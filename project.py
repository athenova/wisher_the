from simple_blogger.generators.YandexGenerator import YandexImageGenerator
from simple_blogger.generators.YandexGenerator import YandexTextGenerator
from simple_blogger import SimplestBlogger
from string import Template
from datetime import datetime
from datetime import timedelta
import time
import os

class Project(SimplestBlogger):
    def __init__(self, **kwargs):
        super().__init__(            
            review_chat_id=-1002374309134,
            topic_word_limit=100,
            image_generator=YandexImageGenerator(),
            text_generator=YandexTextGenerator(),
            #blogger_bot_token_name='WISHER_BOT_TOKEN',
            **kwargs)
        self.channel_desc = {
            'class5nik': 'Школьные предметы 5 класса',
            'have_the_nice_day': 'Мир прекрасен',
            'conscious_child': 'Любовь дочери к матери',
            'conscious_mother_the': 'Любовь матери к дочери',
            'illustrator_the': 'Иллюстрции к книгам',
            'ai_tarot': 'Гороскопы таро',
            'horo_ai': 'Гороскопы',
            'aries_the': 'Гороскопы Овнов',
            'pisces_the': 'Гороскопы Рыб',
            'gemini_the': 'Горосокопы Близнецов',
            'capricorn_the': 'Гороскопы Козерогов',
            'aquarius_the': 'Гороскопы Водолеев',
            'lux_nexus': 'Гармония между всеми аспектами жизни',
            'meloman_the': 'Иллюстрации к песням',
            'one_day_skill': 'Новые навыки каждый день',
            'one_day_word': 'Новые слова каждый день',
            'place_of_interest': 'Достопримечательности',
            'the_force_nexus': 'Места силы',
            'theory_the': 'Различные теории',
            'cto_in_fire': "Будни технического директора",
            'verge_of_breakdown': 'Будни проектного менеджера',
            'coffee_and_nerves': "Будни HR-директора",
        }

    def _example_task_creator(self):
        
        prompt_08_03 = Template(f"Поздравь подписчиц канала c тематикой '$theme' с праздником 8 марта, используй смайликии, используй не более {self.topic_word_limit} слов")
        image_08_03 = Template(f"Нарисуй для подписчиц канала c тематикой '$theme' картину вдохновлённую праздником 8 марта")
        
        result = {}
        for key in self.channel_desc:
            result[f"{key}_08_03_prompt"] = prompt_08_03.substitute(theme=self.channel_desc[key])
            result[f"{key}_08_03_image"] = image_08_03.substitute(theme=self.channel_desc[key])

        return [result]
    
    def _task_extractor(self, tasks, days_offset=None):
        days_offset = days_offset if days_offset is not None else timedelta(days=0)
        task = super()._task_extractor(tasks, days_offset)
        check_date = datetime.today() + days_offset
        check_attr = check_date.strftime('%d_%m')
        attr_to_del = []
        for name in task:
            if not check_attr in name: attr_to_del.append(name)
        for attr in attr_to_del:
            del task[attr]
        return task if len(task) > 0 else None
    
    def revert(self):
        self.init_project()
        os.remove(self.tasks_file)
    
    def _system_prompt(self, _):
        return f"Ты - профессиональный ведущий праздников, церемониймейстер, тамада с огромным словарным запасом"
    
    def review(self, type=None):
        if type is None:
            for channel in self.channel_desc:
                super().review(f"{channel}_08_03") 
                time.sleep(60)
        else:
            super().review(type) 

    def send(self, type=None, image_gen=True, text_gen=True, chat_id=None, days_offset=None, force_text_regen=True, force_image_regen=True):
        if type is None:
            for channel in self.channel_desc:
                super().send(f"{channel}_08_03", image_gen, text_gen, f"@{channel}", days_offset, False, False)
                time.sleep(5)
        else:
            super().send(type, image_gen, text_gen, chat_id, days_offset, force_text_regen, force_image_regen)
            
