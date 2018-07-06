###################################################################
# DO NOT TOUCH THIS CODE -- BEGIN
###################################################################
import threading

def synchronized_method(method):

    outer_lock = threading.Lock()
    lock_name = "__"+method.__name__+"_lock"+"__"

    def sync_method(self, *args, **kws):
        with outer_lock:
            if not hasattr(self, lock_name): setattr(self, lock_name, threading.Lock())
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kws)

    return sync_method

class Singleton:

    def __init__(self, decorated):
        self._decorated = decorated

    @synchronized_method
    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

import six

def package_dirname(package):
    """Return the directory path where package is located.

    """
    if isinstance(package, six.string_types):
        package = __import__(package, fromlist=[""])
    filename = package.__file__
    dirname = os.path.dirname(filename)
    return dirname


import os, sys, shutil, filecmp, platform as pf

@Singleton
class SRWLibSwitcher(object):
    has_switched = False

    @synchronized_method
    def switch(self):
        if not self.has_switched:
            if "darwin" in sys.platform:
                platform = "darwin"
                file     = "srwlpy.so"
            elif "linux" in sys.platform:
                if "debian" in pf.platform():
                    platform = os.path.join("linux", "debian")
                else:
                    raise NotImplementedError("This distribution of Linux is not supported")

                file     = "srwlpy.so"
            elif "win" in sys.platform:
                platform = "windows"
                file     = "srwlpy.pyd"
            try:
                lib_path = os.path.join(package_dirname("srwlpy_aux"), platform, file)
                srw_path = os.path.join(lib_path.split("srwlpy_aux")[0], file)

                do_copy = True
                if os.path.exists(srw_path) and filecmp.cmp(lib_path, srw_path):
                    do_copy = False

                if do_copy:
                    shutil.copyfile(lib_path, srw_path)
                    print("File: ", lib_path, "copied to: ", srw_path)
                else:
                    print("SRW lib switcher not necessary")
            except Exception as e:
                print("SRW: problem during lib switching: " + str(e))

            self.has_switched = True

###################################################################
# DO NOT TOUCH THIS CODE -- END
###################################################################

SRWLibSwitcher.Instance().switch()
