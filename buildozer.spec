[app]

# (str) Title of your application
title = 智能扫码器

# (str) Package name
package.name = smartscanner

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2 as strftime(3) datetime object, leave empty to disable)
# release_pattern = 

# (int) Numerical version - starts at 1 each time you increment
# version_code = 1

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB and #AARRGGBB
presplash.color = #FFFFFF

# (string) Icon of the application
#icon.filename = %(source.dir)s/icon.png

# (string) Splash screen of the application
#splash.filename = %(source.dir)s/splash.png

# (string) URL of application homepage
homepage = http://www.example.com

# (string) Domain of your application
domain = example.com

# (str) Name of the icon for the home screen
icon.filename = %(source.dir)s/icon.png

# (str) Permissions
android.permissions = CAMERA, VIBRATE, FLASHLIGHT, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) Used library or internal packages
requirements = python3, kivy==2.0.0, pillow, openpyxl, pyzbar, opencv-python, jnius, plyer

# (str) The storage location of SDL2 / Kivy (/sdcard ...)
android.sdl2_aars_path = sdl-aars

# (str) The storage location of local/binaries
android.local_aars_path = libs

# (list) Application store permissions
# Should be near the hardware specific entry above
android.add_compile_options = --target-sdk-version 30

# (list) Gradle dependencies to add
#android.gradle_dependencies = com.google.android.gms:play-services-ads:9.0.0

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android specific commit to use, if using a fork
#p4a.commit = HEAD

# (str) python-for-android directory to use (if p4a.source_dir is defined)
#p4a.source_dir =

# (str) Path to a custom ndk
#android.ndk_path =

# (str) Java compiler version
#android.java_compiler = 8

# (list) Android additional libraries to copy into native/libs
#android.add_libs_armeabi_v7a = libs/android/*.so
#android.add_libs_arm64_v8a = libs/android-arm64/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project directories to add (will be added in the
# project.properties of the app)
#android.library_references =

# (list) Android shared libraries which will be copied to the final apk
#android.shared_libraries =

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Size of the generated bitmask used to mark freed memory (in Mebibytes)
#android.heap_size = 512

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) Source files to collect assets from (MANDATORY)
asset.dir = assets

# (list) Black list of extension to ignore when copying assets
# Leave them commented to allow an automatic selection based on the asset extensions
# (used during both compilation and installation stages)
#asset.extensions = png,jpg,jpeg,data,bin,apk,mkv,mp4,avi,flac,wav,mid,midi,xmf,ogg,opus,acc,mpg,mpga,amr,awb,aac,oga,ogv,ogm,spx,epub,zip,tflite

# (list) Native libraries to copy inside the resulting APK
#android.libs = 

# (str) Bootstrap to use for android builds
android.bootstrap = sdl2

# (int) Android API to use
#android.api = 30

# (int) Minimum API required
#android.minapi = 21

# (int) Target API to use
#android.target = 30

# (str) Specify the layout of the main activity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Unpackaged dist name
#android.dist_name = my_dist_name

# (str) Directory name of the created distribution
#android.build_dist_name = my_dist_name

# (bool) Define if the Android App uses big numeric IDs (typically greater than 2147483647)
# Needed for apps with many resources including images larger than 2MB
#android.use_new_asset_ids = False

# (list) Python recipes to install
#p4a.recipes =

# (str) Override the Android manifest template path (was done before build.py but now is done in the buildozer before calling p4a
# Uses format: dirname/source.ext
# For example, you can copy base AndroidManifest.xml into a subdir, and then do:
#android.manifest_template = mydir/AndroidManifest.tmpl

# (list) Compile requirements needed for move-to-target functionality
# Needs to be compiled in the host python platform
# compile_requirements = Cython==0.29.19

# (str) Global debug flag
# Set it to 1 to enable gdb debugging, 0 to disable
#android.global_debug = 0

# (str) Storage method for device target
# By default, the storage is automatically computed depending on how
# the build setup is done. If forced, it can be set to 'public' or 'private'
#android.storage_method = public

# (int) Copy limit (max number of files at once)
#android.copy_limit = 100

# (str) How to copy files to device target
# By default, the best strategy is chosen depending on the build setup
# Values: 'cp', 'rsync', 'sync'
#android.copy_type = sync

# (list) Recipe control flags (format: recipe=flag)
# These correspond to certain recipe-specific commands that can be passed to the build process
#recipe.control_flags = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = Yes, 1 = No)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------


[app]

# New additions for proper Android compatibility:

# Buildozer needs these settings to work properly with Android
android.archs = arm64-v8a, armeabi-v7a

# Additional gradle options
android.add_compile_options = --no-version-vectors

# Request legacy storage for better compatibility
android.add_gradle_repositories = https://google.bintray.com/exoplayer
