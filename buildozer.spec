[app]
title = AdMobApp
package.name = app_by_bhavi
package.domain = org.test_bhavi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,gif,mp4
version = 0.1

# Requirements mein cython ka version lock kiya gaya hai
requirements = python3, kivy==2.2.1, kivymd, pyjnius, android, pyparsing, cython==0.29.33

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCESS_NETWORK_STATE, AD_ID

# API Levels
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

# AdMob Meta-data
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713

# Dependencies
android.gradle_dependencies = "com.google.android.gms:play-services-ads:22.4.0", "androidx.appcompat:appcompat:1.6.1", "androidx.core:core:1.9.0"

android.enable_androidx = True

# Java compatibility fix for Java 17
android.add_compile_options = "sourceCompatibility = 11", "targetCompatibility = 11"

# Architecture
android.archs = arm64-v8a

p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
