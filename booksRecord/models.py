from django.db import models

# Create your models here.

class Book (models.Model):
    '''
    Модель описывает любые книги в хранилище, будь то
    учебники или художественную литературу.
    Если книги имеют одинаковые наименования,
    но разные года, то они считаются разными.\n
    Здесь хранится не каждый экземпляр книги, а только их описания.
    К примеру, в хранилище есть 100 книг «Алгебра. 7 класс», 
    при этом в этой модели хранится ТОЛЬКО ОДНА запись.
    '''
    # the comment above ↑ is to automatically generate a documentation
    # You should write such comments for everything you make.
    # Read more here: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/admindocs/
    
    name = models.CharField(
        max_length=65, 
        db_index=True, 
        unique = True, 
        verbose_name="название",
        help_text = 'Официальное название книги'
    )
    
    authors = models.ManyToManyField(
        'Author',
        verbose_name = "автор(-ы)",
        help_text = '''Автор или авторы книги, \
ссылается на :Model:`booksRecord.Author`'''
    )
    
    publisher = models.ForeignKey(
        'Publisher',
        on_delete=models.PROTECT,
        db_index=False,
        verbose_name='издательство'
    )
    
    year_of_publishing = models.SmallIntegerField(
        verbose_name="год издания"
    )
    
    edition = models.SmallIntegerField(
        verbose_name='номер издания'
    )
    
    inventory_number = models.SmallIntegerField(
        verbose_name='инвентарный номер'
    )
    
    publishing_city = models.CharField(
        max_length=30,
        verbose_name="город издания",
        help_text = 'город издания книги, без "г. "'
    )
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

class Author (models.Model):
    '''
    Модель описывает всех авторов книг в библиотеке,
    Ф.И.О. заполняется полностью.\n
    Правильно:\n
    \tФамилия:\tПушкин\n
    \tИмя:\tАлександр\n
    \tОтчество:\tСергеевич\n
    Неправильно:\n
    \tФамилия:\tПушкин\n
    \tИмя:\tА.\n
    \tОтчество:\tС.\n
    Для записи иностранных авторов 
    использовать кириллицу, отчество
    можно не указывать.\n
    Правильно:\n
    \tФамилия:\tЛондон\n
    \tИмя:\tДжек\n
    \tОтчество:\t\n
    Неправильно:\n
    \tФамилия:\tLondon\n
    \tИмя:\tJack\n
    \tОтчество:\tGriffith
    '''
    
    second_name = models.CharField(
        max_length=25,
        verbose_name='фамилия',
        blank=False,
        help_text='Фамилия автора кириллицей'
    )
    
    first_name = models.CharField(
        max_length=25,
        verbose_name='имя',
        blank=False,
        help_text='Имя автора кириллицей'
    )
    
    middle_name = models.CharField(
        max_length=25,
        verbose_name='отчество',
        blank=True,
        help_text='Отчество автора кириллицей, необязательно'
    )
    
    @property
    def full_name(self):
        '''
        возвращает полное имя автора.\n
        Например: Пушкин Александр Сергеевич
        '''
        return ' '.join((
            self.second_name, 
            self.first_name, 
            self.middle_name
        ))
    
    @property
    def short_name(self):
        '''
        возвращает короткое имя автора.
        Например: Пушкин А. С.
        '''
        '''
        The if below is required
        because the Index out of bounds will be raised,
        if the person hasn't a middle_name (try do ''[0] + '.')
        '''
        
        if self.middle_name:
            _middle_name = self.middle_name[0] + '.'
        else: _middle_name = ''
        
        return ' '.join((
            self.second_name,
            self.first_name[0] + '.',
            _middle_name
        ))
    
    def __str__(self):
       return self.short_name
       
    class Meta:
        ordering = ['second_name','first_name','middle_name']
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

class Publisher (models.Model):
    '''
    Модель описывает каждое издательство,
    в название не надо писать форму собственности
    предприятием (слова "ООО", "ПАО"), а также само
    слово "Издательство".\n
    Правильно:\n
    \tНаименование:\tЭксмо\n
    Неправильно:\n
    \t Наименование:\tООО "Издательство "Эксмо"
    '''
    name = models.CharField(
        max_length=65, 
        db_index=True, 
        unique = True, 
        verbose_name="наименование",
        help_text = '''Официальное наименование 
издательства, без слов "Издательство", "ООО", "ПАО" и т. п.'''
    )
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
        verbose_name = 'издательство'
        verbose_name_plural = 'издательства'