from site_handlers import BaseHandler


class PrintersHandler(BaseHandler):
    def get(self):
        return self.render_template('printing/index.html')