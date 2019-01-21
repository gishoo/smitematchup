from flask import Flask, render_template
import os


def create_app():
   """
   Create a flask application using the app factory pattern.

   :return: Flask app
   """

   app = Flask(__name__, instance_relative_config=True)

   app.config.from_object('config.settings')
   app.config.from_pyfile('setting.py', silent=True)

   @app.route('/')
   def index():
      """Returns the index page"""
      return 'MAKE an Index page'


   @app.route('/build/')
   @app.route('/build/<char>')
   def load_char(char=None):
      """Accumulates the variables needed the character selection screen and passes them"""
      #remove this and pull char names from database
      char_list = ['Achilles','Bellona','Guan Yu','Mercury','Sol','Agni','Cabrakan','Hachiman','Neith','Sun Wukong','Ah Muzen Cab','Camazotz','Hades','Nemesis','Susano','Ah Puch','Cerberus','He Bo','Ne Zha','Sylvanus','Amaterasu','Cernunnos','Hel','Nike','Terra','Anhur','Chaac','Hercules','Nox','Thanatos','Anubis',"Chang'e",'Hou Yi','Nu Wa','The Morrigan','Ao Kuang','Chiron','Hun Batz','Thor','Aphrodite','Chronos','Isis','Osiris','Thoth','Apollo','Cu Chulainn','Izanami','Poseidon','Tyr','Arachne','Cupid','Janus','Ra','Ullr','Ares','Da Ji','Jing Wei','Raijin','Vamana','Artemis','Discordia','Kali','Rama','Vulcan','Artio','Erlang Shen','Khepri','Ratatoskr','Xbalanque','Athena','Fafnir','Kukulkan','Ravana','Xing Tian','Awilix','Fenrir','Kumbhakarna','Scylla','Ymir','Bacchus','Freya','Kuzenbo','Serqet','Zeus','Bakasura','Ganesha','Loki','Skadi','Zhong Kui','Bastet','Geb','Medusa','Sobek']
      char_list.sort()

      #num_chars should get its value from the num of records in the database change batch_num aswell
      #batches is the number of columns that will appear on the character list page
      num_chars = len(char_list)
      batches = 7
      batch_num = num_chars // batches
      batch_list = []

      for num in range(batches):
         tmp_list = []
         for count in range(batch_num+1):
            tmp = num + count * batches
            if tmp <= num_chars-1:
               tmp_list.append(char_list[tmp])
         batch_list.append(tmp_list)

      #fill dict with the variables needed for the templates
      var_dict = {"char":char, "batch_list":batch_list }
      return render_template("char_build.html", **var_dict)


   @app.route('/view/')
   @app.route('/view/<char>')
   def view_char(char=None):
      """ """
      return render_template("god.html", char=char)


   return app
