from site_handlers import BaseHandler
import datetime


class MainHandler(BaseHandler):
    def get(self):
        dt = datetime.datetime.now()
        date = dt.strftime('%d.%m.%Y @ %H:%M:%S')
        params = {'message': 'This is me the MainHandler', 'date': date}
        return self.render_template("index.html", params=params)


class AboutHandler(BaseHandler):
    def get(self):
        return self.render_template('basic/about.html')
