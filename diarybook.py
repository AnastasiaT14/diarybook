import datetime




class Diary:
    last_id = 0

    def __init__(self, memo, tags=' ', owner=None):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        self.owner = owner

        Diary.last_id += 1
        self.id = Diary.last_id

    def match(self, filter_text):
        return filter_text in self.memo or filter_text in self.tags

class DiaryBook:
    def __init__(self):
        self.diaries = []

    def new_diary(self, memo, tags=' ', owner=None):
        self.diaries.append(Diary(memo, tags, owner))

    def search_diary(self, filter_text, owner=None):
        filtered_diaries = []
        for diary in self.diaries:
            if diary.match(filter_text) and (owner is None or diary.owner == owner):
                filtered_diaries.append(diary)
        return filtered_diaries
