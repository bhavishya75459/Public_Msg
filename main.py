from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform

KV = '''
MDScreen:
    md_bg_color: 1, 1, 1, 1

    MDLabel:
        text: "Simple KivyMD AdMob App"
        halign: "center"
        pos_hint: {"center_y": 0.6}
        theme_text_color: "Primary"

    MDLabel:
        text: "Banner Ad will show at bottom"
        halign: "center"
        pos_hint: {"center_y": 0.5}
'''

# Android AdMob Setup
if platform == "android":
    from jnius import autoclass
    from android.runnable import run_on_ui_thread

    AdView = autoclass('com.google.android.gms.ads.AdView')
    AdSize = autoclass('com.google.android.gms.ads.AdSize')
    AdRequestBuilder = autoclass('com.google.android.gms.ads.AdRequest$Builder')
    MobileAds = autoclass('com.google.android.gms.ads.MobileAds')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    FrameLayoutParams = autoclass('android.widget.FrameLayout$LayoutParams')

    @run_on_ui_thread
    def show_banner():
        activity = PythonActivity.mActivity
        MobileAds.initialize(activity)

        adview = AdView(activity)
        adview.setAdSize(AdSize.BANNER)

        # ✅ Test Banner Ad Unit ID
        adview.setAdUnitId("ca-app-pub-7264801834502563/6725695296")

        adRequest = AdRequestBuilder().build()
        adview.loadAd(adRequest)

        params = FrameLayoutParams(
            FrameLayoutParams.MATCH_PARENT,
            FrameLayoutParams.WRAP_CONTENT
        )

        activity.addContentView(adview, params)


class AdApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        if platform == "android":
            show_banner()


AdApp().run()
