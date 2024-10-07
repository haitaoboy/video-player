import webview
import wx
import yaml


class DisplayFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(DisplayFrame, self).__init__(*args, **kw)
        self.browser = None
        self.panel = wx.Panel(self, wx.ID_ANY)

        self.static_text = wx.StaticText(self.panel, label="播放地址：")
        self.font = self.static_text.GetFont()
        self.font.PointSize += 4
        self.font = self.font.Bold()
        self.static_text.SetFont(self.font)

        self.text_ctrl = wx.TextCtrl(self.panel)
        size = self.text_ctrl.GetSize()
        self.font2 = self.text_ctrl.GetFont()
        self.font2.PointSize += 2
        self.font2 = self.font2.Bold()
        self.text_ctrl.SetFont(self.font2)

        self.button = wx.Button(self.panel, wx.ID_ANY, "播放")
        self.font3 = self.button.GetFont()
        self.font3.PointSize += 2
        self.font3 = self.font3.Bold()
        self.button.SetFont(self.font3)
        self.Bind(wx.EVT_BUTTON, self.on_button_click, self.button)

        with open('sources.yml', encoding='utf-8') as f:
            items = yaml.safe_load(f)
            self.sources_name = [item['name'] for item in items]
            self.sources_map = {item['name']: item for item in items}

        self.sources_combox = wx.ComboBox(self.panel,
                                          id=wx.ID_ANY,
                                          value=self.sources_name[0] if len(self.sources_name) > 0 else '',
                                          choices=self.sources_name)
        self.font4 = self.sources_combox.GetFont()
        self.font4.PointSize += 2
        self.font4 = self.font4.Bold()
        self.sources_combox.SetFont(self.font4)

        self.form_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.form_sizer.Add(self.static_text, 0, wx.ALL | wx.CENTER, 5)
        self.form_sizer.Add(self.text_ctrl, 1, wx.ALL | wx.CENTER, 5)
        self.form_sizer.Add(self.sources_combox, 0, wx.ALL | wx.CENTER, 5)
        self.form_sizer.Add(self.button, 0, wx.ALL | wx.CENTER, 5)

        self.out_sizer = wx.BoxSizer(wx.VERTICAL)
        self.out_sizer.Add(self.form_sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizer(self.out_sizer)
        self.CreateStatusBar()
        self.SetStatusText("声明：本软件开放源代码，仅供学习交流使用。")

        self.out_sizer.Fit(self)

        icon = wx.Icon('video.ico', type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        size = self.GetSize()
        size[0] += 500
        self.SetSize(size)

    def on_button_click(self, event):
        url = self.text_ctrl.GetValue()
        if not url:
            return

        name = self.sources_combox.GetValue()
        if not name:
            return

        target_url = "%s?%s=%s" % (self.sources_map[name]['source_url'], self.sources_map[name]['param_name'], url,)
        self.browser = webview.create_window(url, target_url)
        webview.start()


if '__main__' == __name__:
    app = wx.App()
    frm = DisplayFrame(None, title='追剧神器 - 版本0.1')
    frm.Show()
    app.MainLoop()
