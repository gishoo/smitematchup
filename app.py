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
      """
      Render a hello world response.

      :return"
      """
      return 'MAKE an Index page'


   @app.route('/build/')
   @app.route('/build/<char>')
   def load_char(char=None):
      """ """
      #remove this and pull char names from database
      char_list = ['Achilles','Bellona','Guan Yu','Mercury','Sol','Agni','Cabrakan','Hachiman','Neith','Sun Wukong','Ah Muzen Cab','Camazotz','Hades','Nemesis','Susano','Ah Puch','Cerberus','He Bo','Ne Zha','Sylvanus','Amaterasu','Cernunnos','Hel','Nike','Terra','Anhur','Chaac','Hercules','Nox','Thanatos','Anubis',"Chang'e",'Hou Yi','Nu Wa','The Morrigan','Ao Kuang','Chiron','Hun Batz','Thor','Aphrodite','Chronos','Isis','Osiris','Thoth','Apollo','Cu Chulainn','Izanami','Poseidon','Tyr','Arachne','Cupid','Janus','Ra','Ullr','Ares','Da Ji','Jing Wei','Raijin','Vamana','Artemis','Discordia','Kali','Rama','Vulcan','Artio','Erlang Shen','Khepri','Ratatoskr','Xbalanque','Athena','Fafnir','Kukulkan','Ravana','Xing Tian','Awilix','Fenrir','Kumbhakarna','Scylla','Ymir','Bacchus','Freya','Kuzenbo','Serqet','Zeus','Bakasura','Ganesha','Loki','Skadi','Zhong Kui','Bastet','Geb','Medusa','Sobek']
      char_list.sort()

      #This is used to define how many cards to show per page
      num_chars = len(char_list)
      batch_num = 10
      last_index = num_chars % batch_num
      batch_char_list = []

      #divides the char list into sub lists and adds it to a list of lists
      count = 0
      total_count = 0
      curr_list = []

      for curr_char in char_list:
         if count == batch_num:
            batch_char_list.append(curr_list)
            count = 0
            curr_list = []
         elif total_count == num_chars-1:
            curr_list.append(curr_char)
            batch_char_list.append(curr_list)
         else:
            curr_list.append(curr_char)
            count += 1
         total_count += 1

      #fill dict with the variables needed for the templates
      var_dict = {"char":char, "batch_list":batch_char_list }
      return render_template("char_build.html", **var_dict)


   @app.route('/view/')
   @app.route('/view/<char>')
   def view_char(char=None):
      """ """
      return render_template("god.html", char=char)


   return app
