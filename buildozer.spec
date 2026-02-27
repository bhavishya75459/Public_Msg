[app]
# (section) Title of your application
title = AdMobApp

# (string) Package name
package.name = app_by_bhavi

# (string) Package domain (needed for android packaging)
package.domain = org.test_bhavi

# (directory) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,gif,mp4

# (string) Application versioning
version = 0.1

# (list) Application requirements
# AdMob ke liye pyjnius aur android zaroori hain
requirements = python3, kivy==2.2.1, kivymd, pyjnius, android, pyparsing

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, AD_ID

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage
android.private_storage = True

# (bool) Accept SDK license
android.accept_sdk_license = True

# (list) Android meta-data (AdMob App ID)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713

# (list) Android libraries to add
android.gradle_dependencies = "com.google.android.gms:play-services-ads:22.4.0", "androidx.appcompat:appcompat:1.6.1", "androidx.core:core:1.9.0"

# (bool) Enable AndroidX
android.enable_androidx = True

# (list) Java compatibility (Updated for Java 17/Gradle 8)
android.add_compile_options = "sourceCompatibility = 11", "targetCompatibility = 11"

# (list) The Android architectures to build for
# Sirf ek architecture rakha hai fast build ke liye
android.archs = arm64-v8a

# (str) python-for-android branch
p4a.branch = master

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
