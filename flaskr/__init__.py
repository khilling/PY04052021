from flask import Flask, render_template
import parser


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )


    @app.route('/')
    def index():
        parser.update()
        return render_template('index.html')

    @app.route('/rbc')
    def rbc():
        return render_template(parser.rbc())

    @app.route('/yaplakal')
    def yaplakal():
        return render_template(parser.yaplakal())

    return app