[app]
title = AdMobApp
package.name = app_by_bhavi
package.domain = org.test_bhavi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,gif,mp4
version = 0.1

# Requirements mein pyjnius zaroori hai AdMob ke liye
requirements = python3, kivy==2.2.1, kivymd, pyjnius, android, pyparsing

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCESS_NETWORK_STATE, AD_ID

# STABLE API LEVELS (Don't use 35 or 36)
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license = True

# Meta-data for AdMob (Test ID)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713

# Dependencies
android.gradle_dependencies = "com.google.android.gms:play-services-ads:22.4.0", "androidx.appcompat:appcompat:1.6.1", "androidx.core:core:1.9.0"

android.enable_androidx = True
android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# Fast Build ke liye sirf ek architecture
android.archs = arm64-v8a

p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
