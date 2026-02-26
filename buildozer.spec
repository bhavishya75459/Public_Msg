[app]

# App Info
title = kivmob_test
package.name = kivmob_test
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Requirements
requirements = python3,kivy,kivymd,android,jnius

orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Android API Settings
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

# ✅ Correct AdMob Dependency (IMPORTANT)
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.6.0

# Enable AndroidX
android.enable_androidx = True

# ✅ Official Google Test App ID (Safe for Testing)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713

android.allow_backup = True
android.copy_libs = 1

# Python for Android
p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 1
