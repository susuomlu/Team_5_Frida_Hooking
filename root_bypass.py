import frida
import time

device = frida.get_usb_device()

pid= device.spawn("com.android.insecurebankv2")
device.resume(pid)
time.sleep(1)

session=device.attach(pid)

hook_script="""

Java.perform(function bypass() {
	console.log('Bypassing root check...')
    var myvar=Java.use("com.android.insecurebankv2.PostLogin");
    myvar.doesSUexist.implementation= function (bypass){
        console.log("---- SU root bypass----");
        return false;
    };
    myvar.doesSuperuserApkExist.implementation=function(bypass){
        console.log("---- SU APK bypass----");
        return false;
    };
})

"""

script=session.create_script(hook_script)
script.load()

input('')