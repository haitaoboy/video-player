import webview
import wx


class VIPFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(VIPFrame, self).__init__(*args, **kw)
        panel = wx.Panel(self)

        st = wx.StaticText(panel, label="追剧神奇 - V0.1")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        self.text = wx.TextCtrl(panel)

        button = wx.Button(panel, wx.ID_ANY, "播放")
        self.Bind(wx.EVT_BUTTON, self.on_button_click, button)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        sizer.Add(self.text, wx.SizerFlags().Border(wx.BOTTOM | wx.LEFT, 25))
        sizer.Add(button)
        panel.SetSizer(sizer)

        self.CreateStatusBar()
        self.SetStatusText("声明：本软件开放源代码，仅供学习交流使用。")

    def on_button_click(self, event):
        url = self.text.GetLineText(0)
        print(url)
        window = webview.create_window('Woah dude!',
                                       'https://jx.2s0.cn/player/analysis.php?v=https://www.iqiyi.com/v_1d60y56w17s.html')
        webview.start()


if '__main__' == __name__:
    app = wx.App()
    frm = VIPFrame(None, title='追剧神奇 - 版本0.1')
    frm.Show()
    app.MainLoop()
