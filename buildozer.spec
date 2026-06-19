[app]
title = Cobros V12 Campo
package.name = cobrosv12campo
package.domain = org.cobrosv12

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,ttf,pdf,sql
source.exclude_exts = spec,db,sqlite,log
source.exclude_dirs = .git,__pycache__,bin,build,.venv,venv,backups,exports,reportes

version = 1.0.0
entrypoint = main.py
icon.filename = assets/icon.png
orientation = portrait
fullscreen = 0

requirements = python3,kivy==2.3.1,plyer,certifi,pyjnius

android.permissions = INTERNET,POST_NOTIFICATIONS,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 34
android.minapi = 24
android.ndk = 25b
android.sdk = 34
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.private_storage = True

android.logcat_filters = *:S python:D
p4a.branch = master
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = ./.buildozer
bin_dir = ./bin
