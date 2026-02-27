[app]

# (str) Title of your application
title = admob

# (str) Package name
package.name = App_by_bhavi

# (str) Package domain
package.domain = org.test_bhavi

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf,gif,mp4

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Added 'play-services-ads' logic via gradle and essential recipes
requirements = python3,kivy==2.2.1,kivymd,jnius,android,pyparsing

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, AD_ID

# (int) Target Android API (API 33 is required by Play Store now)
android.api = 33

# (int) Minimum API
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (list) Android application meta-data (AdMob App ID)
# Test ID use kiya hai, real ID se baad mein replace kar lena
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713

# (list) Gradle dependencies
# Firebase-ads ki jagah play-services-ads (Modern way)
android.gradle_dependencies = "com.google.android.gms:play-services-ads:22.4.0", "androidx.appcompat:appcompat:1.6.1", "androidx.core:core:1.9.0"

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Java compile options (IMPORTANT for AdMob/Modern SDKs)
android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) The Android archs to build for
# Dono archs rakhe hain, agar build fail ho toh sirf arm64-v8a rakhein
android.archs = arm64-v8a, armeabi-v7a

# (str) python-for-android branch
p4a.branch = master

[buildozer]

# (int) Log level (2 = debug info)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
