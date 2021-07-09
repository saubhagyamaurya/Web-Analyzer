import requests
import lxml.html.clean
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords as sw
import nltk

def getUrlContent(url):
    #Downloads and returns content
   return requests.get(url, timeout = 20).content


def cleanme(content):
  #Removing all tag and scripts from the scrapping data
    cleaner = lxml.html.clean.Cleaner(
        allow_tags=[''],
        remove_unknown_tags=False,
        style=True,
    )
    html = lxml.html.document_fromstring(content)
    html_clean = cleaner.clean_html(html)
    return html_clean.text_content().strip()



def contentProcessing(content):
  text_token = wt(content)
  #print(text_token)
  wordwithoutsw = [word for word in text_token if not word in sw.words()]
  wordswithfrequencies = nltk.FreqDist(wordwithoutsw)
  wordset = set(wordwithoutsw)
  #print(wordset)
  
  #print(type(wordswithfrequencies))
  keyvaluespairs = wordswithfrequencies.items()
  n = len(wordswithfrequencies)
  #wordswithfrequencies.plot(n,cumulative=False)
  return wordset,keyvaluespairs



currenturl = "https://www.w3schools.com/java/"

htmlpage = getUrlContent(currenturl)
content = cleanme(htmlpage)
wordset, keyvaluepairs = contentProcessing(content)


dharmiksite=set(["Sarovar","holiest","travel","Pandava","Rameshwar","temple","booking","Dharmic","Heritage","Mandirs","Ghats","Rivers",
"Ghat","River","Ganga","Viswanath","Prakriti","Hindus","Linga","Yatra","TempleKashi","Prasadam","Lord","Teerath","Shiva","Maharani","Baba",
"Donation","shrikashivishwanathtempletrust","Mythology","TEMPLE","Kund","ease-of-darshan","Kund"])

schoolorcollege = set(["STUDENTS","Assistant","designing","Polytechnic","Technology","educational","diploma","department","Eeducation",
"Colleges","Institute","Management","Examination","Computer","Science","Engg","Academics","IT","Chemical","Engineering","Civil",
"Electronics","Electrical","Mechanical","Garment","Applied","Humanities","Courses","Information","Technology","Automobile","Production",
"Admission","Lateral","Training","Alumni","Ragging","Placement","Welfare","Lecture","FACULTY","Toppers","Branch","Rank","Holders","Cyber",
"security","institution","Lab","knowledge"])

programmingtutorial = set(['Keylogger', 'Features', 'IndexingNumpy', 'Notes', 'cutting', 'experience', 'Using', 'AnalysisData', 'value', 
'WiproCrack', 'TCS', 'SetsPython', 'bit_length', 'askquestion', '8', 'PythonPrecision', 'ConceptsPython3', 'Birthday', 'Chatting', 'Geek',
'AlgebraNumpy', 'ModelForm', 'LanguagePython', 'PythonNumpy', 'MongoDBPython', 'TkinterMessage', 'time', 'Geeks', 'Noida', 'PythonGlobal',
'NewAd', 'InterviewsCompetititve', 'Converting', 'OrderedDict', 'ModelFormSetsDjango', 'Feature', 'PandasPandas', 'Implementation', 
'Deleting', 'Numpy', 'InstallationNavigating', 'allows', 'handwritten', 'Advanced', 'PythonPerforming', 'pythonOperator', 'operators', 
'post', 'PythonMachine', 'SeriesPython', 'NotesClass', 'CourseCompetititve', 'Otsu', 'Misc', 'windowPython', 'except','makes', 
'TemplatesViews', 'Industry', 'rows', 'Coding', 'ProjectsPython', 'AnalysisWhat', 'Textinput', 'OpenCVExtract', 'codeBirthday',
'insert_one', 'Label', 'ArticleWrite', 'PythonExceptions', 'Thresholding', 'fulfilled', 'Translator', 'questions', 'Arithmetic', 'Edge', 
'Creating', 'free', 'instance', 'Companies', 'program', 'webcamPython', 'needs', 'PythonTaking', 'FilteringPython', 'StackLayout', 
'geographical', 'less', 'error', 'Canvas','RegressionCancer', 'Extracting', 'Structures', 'SystemRecommended', 'Test', 'pythonDesigning',
'Notifier', 'pythonByte', 'pythonFB', 'HTML', 'widely', 'general-purpose', 'FormsRender', 'Bilateral', 'int', 'IIIUGC', 
'SyllabusImportant','Local', 'SystemML', 'handlingFile', 'form', 'Algorithms', 'PythonOperatorsBasic', 'scrollbarPython', 'EngineeringWeb',
'append', 'widgetsDjango', 'SMS', 'Paced', 'Image', 'FormsViews', 'CountingRandom', 'etc.My', 'methodDealing', 'Competitive', 'Detection',
'StructureHow', 'Visited', 'PythonLooping', 'Set-1', 'service-based', 'QuestionsInterview', 'pythonPython', 'programming', 'DataDjango',
'languageImportant', 'columns', 'concepts', 'PandasRead', 'range', 'TutorialsPracticeCoursesCompany-wiseTopic-wiseHow', 'ModelApplying', 
'TutorialIntroduction', 'large', 'JavaScriptjQuerySQLPHPScalaPerlGo', 'ArchitectureMost', '-1Logic', 'Scope', 'ConquerBacktrackingBranch',
'Bokeh', 'AlgorithmsGreedy', 'validation', 'OperationsNumpy', 'Layout', 'strong', 'geeksforgeeks', 'defined', 'CreationNumpy', 
'SpinBoxProgressbar', 'OpenCVErosion', 'Pythonclass', 'scraping', 'PythonWhen', 'read', 'Difference', 'PythonDivision', 
'PythonDeserialize', 'create', 'prepare', 'kivy', 'LimitationsComponents', 'network', 'Intermediate', 'write', 'to_bytes', 'possible',
'Identifying', 'Mantri', 'exampleKeywords', 'Program', 'Relative', 'frameworks', 'acknowledge', 'well','input', 'Binding', 'SQLite', 
'Add', 'PythonOpenCV', '10', 'ComputationCompiler', 'Courses', 'tutorialPython', 'Input', 'Floor', 'TutorialPython', 'LoopsSolving', 
'interviews', 'Dropdown', 'programs', 'ExamUGC', 'Company', 'Chains', 'PythonWriting', 'PythonFunctionsFunctions', 'Control', 'Google', 
'SortMongoDB', 'PythonCollections.UserList', '1', 'QuizzesGATEGATE', 'PythonPython-Tkinter', 'Series', 'DesignDigital', 
'HandlingException', 'OpenCVPython', 'install', 'Learn', 'PythonDefaultdict', 'TutorialSelenium', 'examples.Below', 'PacedStart',
'Dropbox', 'Wikipedia', '*', 'FindPython', 'While', 'Toplevel', 'online', 'formating', 'KivyGridLayouts', 'operations', 'Calculator100', 
'PythonMake', 'Pradesh', 'booleanTernary', 'Gates', 'effectivelyPython', 'pythonC/C++', 'JobsCome', 'suited', 'PyTorchPython', 'Tracker',
'New', 'APIFetching', 'Processing', 're.search', 'OperatorsData', 'Netflix', 'GATE', 'MongoDB', 'feedback', 'user', 'Please', 
'Multi-threading', 'variablePrivate', 'Original', 'Checkbutton', 'PageLayout', 'Windows', 'Filter', 'Order', 'Instagram', 'TuplesPython', 
'functionsPython', 'MySQLPython', 'migrationNews', 'PythonCollections.UserDict', 'Searching', 'Maths', 'ModelsDjango', 'object', '.', 'kwargsPython',
 'get', 'methodPython', 'Comment', 'TutorialsAlgorithmsAnalysis', 'CampusGblog', 'Addition', 'PatternsMultiple', 'files', 'Progress', 'FunctionNumpy', 
 'Sharding', 'languages', 'pandas.read_csv', 'pythonFunctionsFunctions', 'help', 'PythonInheritance', 'cookies', 'TkinterReal', 'collection', 'DSA', 
 'ArchitectureTheory', 'easiest', 'Deep-Learning', 'StringPython', 'insert_many', 'techniques', 'elseChaining', 'drop_index', 'MySQL-Connector', 
 'TutorialOpenCV', 'Sector-136', 'static', 'Tkinter', 'pythonGenerators', 'sampling', 'Try', 
'GET', 'TutorialGeeksforgeeks', 'DataPython', 'random_sample', 'Java', 'expertsPremiumGet', 'Metaclasses', 'Personal', 'TutorialLinear', 
'Techniques', 'Cup', 'parameter', 'DFSMenu', 'problem-solving', 'PythonFace', 'Learning', 'PandasConversion', 'How', 'Level', 'status', 
'applicationsDownload', 'PandasPython', 'Facebook', 'Delete_many', 'Science', 'find', 'URL', 'PreparationTop', 'phone', '1Namespaces', 
'TkinterSimple', 'pythonChanging', 'QueryPython', 'functionUsing', 'treeview', 'NotesNCERT', 'Project', 'Validating', 'Guide', 'keyword', 'With', 
'ListBox', 'pythonPacking', 'Course', 'PythonNamedtuple', 'currency', 'PythonDatabase', 'variableSwap', 'values', 'using', 'language', 'SubjectsVideo', 
'PrintingInheritance', 'And', 'PythonSocket', 'instead', 'generate', 'ScrollbarPython', 'SolutionRD', '5th', 'ExperienceInternshipsVideos', 'PythonLocator', 
'attributeReflectionGarbage', 'tkinterSimple', 'PapersISRO', 'language.Python', 'edge', 'paradigms.Python', 'Computer', 'Carousel', 'PythonOperator', 'Match', 
'Jun', 'means', '1SQL', 'video', 'args', 'preparation', 'Do', 'Oriented', 'QuestionsBasicsPython', 'wordsFacebook', 'PythonChainMap', 'Uses', 'DatabaseMongoDB', 
'Module', "'Space", 'Data', 'IIUGC', 'PythonMongoDB', 'integer', 'pythonelse', 'csv', 'CourseView', 'DetailsDSA', '–', 'applicationPython-Tkinter', 'linesMorse', 
'JSONWorking', 'String', 'Essential', 'dtype', 'pythonInplace', 'Restaurant', 'Self', 'operatorDivision', 'Shortening', 'NET', 'images', 'JSONPython', 'button', 
'Bound', '&', 'PapersGATE', 'game', '#', 'Parse', 'ClausePython', 'Columns', 'TkinterPython', 'CSV', '@', 'reminder', 'KeysGATE', '(', 'Software', '2Namespaces', 
'forswitch', 'MySQLConnect', 'bit', 'LearningWeb', 'Tips', 'bitwise', 'LogicSoftware', 'content', 'experienced', 'TutorialInstalling', 'type', 'Verbose', 'LoopsPython', 
'JoinPython', 'coding', 'notationsLower', 'TechnologiesHTMLCSSJavaScriptAngularJSReactJSNodeJSBootstrapjQueryPHPSchool', 'qr', 'PythonAction', 'Regex', 'PythonStatement', 
'TheoryAnalysis', 'PythonInput', 'superPolymorphism', 'Read', 'NLP', 'understand', 'membersConstructors', 'DataFrameWorking', 'A-118', 'Continue', 'web', 
'StructureMatrixStringsAll', 'b', 'Array', 'Indexing', 'Average', 'Updating', 'Synchronization', 'training', 'Functions', 'randint', 'Refer', 'All', 'Function',
'standard', 'Strings', 'blurring', '18', 'PythonDeque', 'reservedWe', 'Webpage', 'Beginners', 'local', 'Programmers', 'PythonHow', 'tech-giant', 'Update', 'PythonAbstract', 
'2SQL', 'advanced', 'website', 'Session3', 'ListsPython', 'Views', 'articles', 'Expression', 'OpenCVHow', 'handlingUser', 'generally', 'Boston', 'Connection', 'PostgreSQLOracle', 
'hacks', 'PythonData', 'analysis', 'LiveGet', 'xrange', 'Kaggle', 'indentation', 'DialogPython', 'relatively', 'crack', 'ORM', 'PythonMetaprogramming', 'PythonClass', 'linked', 
'Preparation', 'Procedural', 'DjangoDjango', 'Regression', 'QuestionSearching', '11', 'iteration', 'programmers', 'Operators', 'DjangoData', 'train', 'Classes', 'Resizing', 'Code', 
'closuresFunction', 'PythonInteracting', 'popular', 'Initialization', 'Overloading', 'KivyData', 'Background', 'ideaWhy', 'access', 'grid', 'PythonHelp', 'PythonWebsite',  
'Interactive', 'Privacy', 'currently', 'basicsPython', 'printing', 'Components', 'BeautifulSoup', 'DetailsMost', 'ModulesOS', 'ExamplesFunctional', 'Artificial', 'Notepad', 
'AlgorithmsAsymptotic', 'Self-Paced', '.iloc', 'BoxLayout', 'used', 'Visualization', 'Object-Oriented', 'Some', 'SystemDBMSComputer', 'Expressions', 'Papers', 'PythonRead', 
'NotesLast', 'AlgorithmsPattern', '’', 'moduleWorking', 'blockerSend', 'Switch', 'FormattingData', 'ufunc', 'ranf', 'MembersData', 'Operator', 'Neural', 'omega', 'time.Python', 
'arrow_drop_upWriting', 'ExceptErrors', 'Membership', 'Create', 'PythonDestructors', 'PythonReading', 'list', 'Bitwise', 'CRUD', 'PythonOpen', 'DataFrameDealing', 'Treeview', 
'CSUGC', 'LoopPython', 'neuron', 'high-level', 'kerascreating', 'round', 'Syllabus', 'Recent', 'Variables', 'Django', 'parameters', 'image', 'top', 'languagesInput/OutputTaking', 
'single', 'affordable', 'without', 'application', '2.x', 'subtraction', 'doubt', 'PythonMisc10', 'string', 'Automating', 'Classification', 'CountingPandasPandas', 'Iterations', 
'Exceptionclean', 'Type', 'Happy', 'PythonEncapsulation', 'Complete', 'TopCareersInternshipJobsApply', 'PythonMYSQLdb', 'pythonPrint', 'tutorial', 'Questions', 
'ProgrammingTestimonialsGeek', 'C++', 'industry', 'topics', 'ArrayNumpy', 'pythonClass', 'ArticlesDatabase', 'IntroductionPython', 'rights', 'newline', 'StructuresLanguagesCC++JavaPythonC', 
'DataTypesStringsListTuplesSetsDictionaryArraysVariablesVariables', 'computingText', 'Mathematical', 'functionHow', 'PracticeC++JavaPythonCompetitive', 'Competition', 'frameworksMultimediaScientific', 
'LanguageHTMLCSSKotlinInterview', 'StructuresAlgorithmsInterview', 'bird', 'Minute', 'Concepts', ';', 'GroupByPython', 'etc', 'technology', 'Exceptions', 'Communication', 'VS', '__iter__', 
'featuredPracticeLearn', 'Joining', 'processes', 'assistance', 'Mongodb', 'Bar', 'queue', 'AppSystem', 'requirement', 'Language', 'Types', 'ExperiencesExperienced', 'technique', 'Hiding', 
'Web-scraping', 'NotesGATE', '9', 'Topics', 'QuestionsPython', 'In', 'Limit', 'KivyPython', 'pyramid', 'biggest', 'MVT', 'DataFrameIterating', 'Programming', '1Operator', 'Lists', 'AdvanceOS', 
'RegexPassword', 'Over','empty', 'strength', 'start-up', 'BoundAll', 'use', 'PythonAny', 'TutorialsPython', 'Reading', 'Text', 'Based',
'PythonNumpyPython', 'LanguageLast', 'PythonMultithreading', 'CodingApplications', 'simple', 'ArticlesMust', 'ListStackQueueBinary', 
'Logistic', 'Practice', 'best', 'ConcatenatingPython', 'NumPyNumPy', 'comptetive', 'Subtraction', 'LearningSchool', 'KivyPython|', 
'lambdaGlobal', 'AnchorLayout', 'Static', 'Scale', 'TypesPython', 'SchemeA', 'asksaveasfile', 'data', 'iteratorPython', 'Entry', 
'functionMaximum', 'Ambassador', 'Framework', 'Policy', 'ClosuresDecorators', 'ExamplesNZEC', '+=', 'Rows', 'Uttar', 
'PythonUser-defined', 'Days', 'Movie', 'Multiple', 'Best', 'Courses:1', 'prices.4', 'return', 'analysisGetting', 'frequent', 
'PythonLocating', 'table', 'processA', 'Float', '2021', 'Structure', 'Pillow', 'Adobe', 'PythonTypes', 'new', 'Cross-platform', 
'DecoratorsDecorators', 'bad', '2021Python', '1Multithreading', 'Generic', 'Convolutional', 'Color', 'star', 'KivyKivy', 
'StatementPython', 'classification', 'many', 'random_integers', 'PythonCollections.UserString', 'foundation', 'sign', 'Exercises', 
'OpenCVOpenCV', 'little', 'from_bytes', 'Set', 'ProgrammingDesign', 'print', 'ModulepprintTimit', 'Tip', 'UsCareersPrivacy', 'Charts', 
'PyQtColor', '201305', 'SolutionClass', 'multi-purpose', 'RegressionUnderstanding', 'MySQL', 'ReturnReturn', 'ExperiencedTraverse',
'Urllib', 'following', 'Merging', 'ObjectsNumpy', 'Search', 'ProgramProjectGeek', 'dream', 'Machine', 'break', 'crawl', 'pythonLogical',
'functionMetaprogramming', 'given', 'PandasBoolean', 'pythonProgram', 'Tuples', '1Inplace', 'TemplatesToDo', 'cell', 'ProgramsHow', 
'TypesIntroduction', 'Set-2', 'Housing', 'Menu', 'AppWeather', 'TkinterWhat', 'company', 'issubclass', 'Missing', '__next__', 
'VersionPython', 'Kivy', 'place', 'TutorialDjango', 'DataFramePython', 'Sharma', 'pack', 'scratch', 'YouTube', 'GeeksforGeeks', 
'ImageArithmetic', 'iterable', 'way', 'JAVA', 'notifierwhatsapp', 'PythonCreate', 'browsing', 'HandlingPython', 'PythonSQL', 
'PythonFirst', 'Pseudo-polynomial', 'JobsPost', 'companies', 'Input/Output', 'For', 'ProgrammingMachine', 'PythonImage', 'Articles', 
'basics', 'Spinner', 'PythonWrite', 'RegexRegular', 'yield', 'Collections', 'StatementLooping', 'graph', 'CasesAsymptotic', 'generating', 
'singly', 'Flow', 'ObjectsConstructors', 'Updated', 'AlgorithmsSorting', 'Updation', 'News', 'Basic', 'Tricks', 'functionPython', 'inputs', 
'interview-centric', 'DigestQuizzesGeeks', 'enhancing', 'ServiceProGeek', 'Basics', 'Android', 'usGeeks', 'datasetPython', 'location', 
'Drop', 'ContributeWrite', 'programmingOptimization', 'pace', 'Network', 'latest', 'System', 'Railway', 'registration', 'facts', 'API',  
'kwargs', 'ModulePython', 'ScrolledText', 'NumPyNumpy', 're.findall', 'CollectionsPython', 'TreeBinary', 'order', 'toolFind', 'Foundation2', 
'Inserting', 'PythonSerializing', 'conversion', 'TkinterCreate', 'Find', 'SubjectsMathematicsOperating', 'SearchingGeometric', 'DictionaryPython', 
'FrameworkPython', 'variables__name__', 'reviewsLearning', 'Database', 'DevelopmentPuzzlesProject', 'expression', 'code', 'KeysISRO', 'generation', 
'Specific', 'COVID-19', 'Retrieve', 'pass', 'fundamentals', 'ad-free', 'Linear', 'AlgorithmsGraph', 'Decision', 'PythonException', 'statementYield', 
'Recommender', 'kivyPython', 'SeleniumDesign', 'Uber…', 'variable', 'Latest', 'FormsetsDjango', 'PythonStructuring', 'GeeksforGeeksSystem', 'LearningGUI', 
'ClusteringPython', 'By', 'console', 'Forms', 'usually', 'WidgetCombobox', 'Generators', '8-11', 'ArticlesIDECampus', 'GUITkinter', 'Update_one', 
'NetworksComputer', 'mnist', 'OOPPython', 'iteratorCoroutine', 'filePython', 'examples', 'PythonBuilt-in', 'DataFrameIndexing', 'product-based', 
'provides', 'ProgrammingDivide', 'lexicographical', 'Object', 'SeleniumSelenium', 'C', ':', 'ArraysControl', 'PythonPolymorphism', 'Examples', 
'unpacking', 'TutorialMachine', 'ide.geeksforgeeks.org', 'text', 'Rotating', 'preparing', 'IdeasSchool', '+', 'basic', 'advantages', 
'MigratePython', 'AlgorithmsDynamic', 'Design', 'Complexity', 'Output', 'designed', 'Seaborn', 'LabelRadioButton', 'Interview', 'PreparationTopic-wise', 
'Astrological', 'Slicing', 'LearningIntroductionPython', 'TkinterModules', 'applications', 'functionNumpy', 'A', 'emotions', 'page', 'job', 
'BokehTableau', 'Special', 'SolutionsClass', 'Plotly', '?', 'Scikit-learnImplementing', 'Upper', 'assign', 'calculator', 
'StructuresLanguagesCS', 'Play', 'interview', 'field', 'us', 'Pandas', 'Set-3', 'FlowPython', 'link', 'Zodiac', 'ProgrammersAmazing', 
'required', 'MessageBox', 'Where', 'TutorialPandas', 'PapersCS', 'file', 'Statements', 'processing', 'WidgetPython', 'functionRandom', 
'Web', 'digits', 'Popular', 'Shifting', 'CS', 'BokehExploratory', 'ask', 'valid', 'operator', 'OperatorsTernary', 
'VisualizationMatplotlib', 'Iterating', 'along', 'Slider', 'Popup', 'Makemigrations', 'database', 'giants', 'CollectionPython', 
'SolutionsPython', 'DataFrameCreating', 'birthTrack', 'SolutionStudentCampus', 'tkinter', 'Working', 'display', 'smaller', 
'InterviewsInternship', 'Desktop', 'pythonChaining', 'inheritance', 'understood', 'CSISRO', 'ConceptMaximum', 'AlgorithmsData', 
'driven', 'RegressionK', 'Organization', 'AnalysisWorst', 'webapp', 'variables', 'Linux', 'import', 'buttons', 'File', 'MonthPlacement', 
'decorators', 'PythonAppend', 'like', 'ViewsClass', 'Amazon', 'Frame', 'Official', 'started', '/', 'stuff', 'Scrapy', 'Widgets', 
'Methods', 'Binary', 'mobile', 'Foundation', 'ItertoolsPython', 'PNR', 'functions', 'NumPy', 'pythonPrograms', 'WidgetHierarchical', 
'Selenium', 'collectionException', 'custom', 'apply', 'heapq', 'widget', 'NotationsLittle', 'PanedWindow', 'ensure', 'makingBasic', 
'Universal', '=', 'ProfessionalsView', 'Choice', 'HomeCoursesGBlogPuzzlesWhat', 'Adaptive', 'languagesHow', 'Solved', 'metaclassesClass', 
'Insert', 'ExceptionBuilt-in', 'classes', 'moduleCalendar', 'comment', 'DatesGATE', 'Cookie', 'WriteCome', 'Scientist/Engineer', 
'geeksforgeeks.orgCompanyAbout', 'statementPython', 'objects', 'trics', 'UsCopyright', 'Multiprocessing', 'PythonPython', 'PyQt', 
'IndexingBasic', 'check', 'InstallationDjango', 'emotion', 'ObjectsData', 'SDE', 'functionImport', 'difference', '2Math', 'python',
'updates', 'Update_many', 'Delete_one', 'stopwatch', 'TutorialKivy', 'running', 'CSVWorking', '3', 'TreeHeapHashingGraphAdvanced', 
'Infobox', 'Identity', 'notControl', 'JobCourses', 'XlsxWriter', 'Building', 'Paper', '3.x', 'method', 'ProgramSchool', 'live','errortry', 
'PythonHeap', 'PythonMemoization', 'App', 'Selecting', 'development', 'readable', 'comparison', 'introductionPython', 'Select', 'Operations', 
'class', '1Regular', 'master', 'CodeWhy', 'Delete', 'JSON', 'PolicyContact', 'Checkbox', 'Encode-Decode', 'ProgrammingVulnerability', 
'2Difference', 'RecurrencesAmortized', 'numpy', 'begin', 'FrameworkDjango', 'GUI', 'Handling', 'etc.The', 'Microsoft', 'TablePython', 
'PythonFile', 'library', 'ValuesPartial', 'always', 'almost', 'create_index', "'s", 'pythonType', 'machine', 'AlgorithmsMathematicalRandomized', 
'site', 'huge', 'news', 'NumpyNumpy', '1Python', 'Approximation', 'Indentation', 'Dataframe/Series.head', 'convertor', 'login', 'level', 'IT', 
'skills', 'SeriesData', 'FormattingOperatorsPython', 'SeriesCreating', 'OpenCV', 'Exception', 'giant', 'Analysis', 'PythonGet', 'Java.This', 
'function', 'continue', 'Python', 'QuizPython', 'ModuleCounters', 'askopenfile', 'Applications', 'share', 'elements', '.loc', 'specifically', 
'Scikit-learnSaving', 'management', 'Dilation', 'PythonIntroduction', 'PythonDjango', 'MonthCampus', 'Scaling', 'efficient', 'Sorting', 
'PremiumView', 'StructuresArraysLinked', 'different', 'arguments', 'Class', 'AlgorithmsPolynomial', 'PythonDecorators', 'PreparationGet', 
'manner', 'learn', 'The', 'Simple', 'Widget', 'codeReading', 'learning', 'visualization', 'tkinterPython', 'Time', 'date', 'here.What', 
'Socket', 'multiple', 'bDifference', '|', 'convenience.5', '__import__', 'Model', 'Jupyter', 'basicsKeywords', 'pythonrange', 'Write', 
'Strategies', 'ExamplesPython', 'Introduction', 'iteratorGenerators', 'sep', 'FlowLoopsLoops', 'Global', 'BasicsDjango', 'specially', 
'actionNzec', 'modelPython', 'CornerCompany', 'PolicyLearnAlgorithmsData', 'vs', '2.xPython', 'Install', 'Modules', 'MessagePython', 
'Projects', 'TopicsClass', 'neural', 'Saving', 'mean', 'Challenge', 'TopicsPractice', 'GeeksforGeeksSkip', 'POST', 'DatabasePython', 
'ndarrayNumpy', 'Images', 'links', 'applicationsInput/OutputTaking', 'app', 'Dataframe.describe', 'Notebook', 'Live', 'condition', 'nodes'
'To', 'LinkedList', 'PYTHON', 'throws', 'JAVA', 'Inheritance', 'simplified', 'Icons', 'Download', 'improve', 'Intelligence', 'missing', 'Modifiers', 
'main', 'If', '»', 'protected', '/', 'certified', 'interface', 'recommend', 'example', 'Python', 'Selector', 'We', 'W3Schools', 
'Exercise', 'code', 'object', 'Cyber', 'https', 'Artificial', 'concepts', 'Accessibility', 'Course', 'report', '!', 'button', 'Type',
'World', 'Break/Continue', 'CERTIFIED', 'Log', '3', 'Science', 'may', 'Loop', 'HashMap', 'Hello', 'UTF-8', 'throw', 'games', 'instanceof',
'public', 'void', 'Attribute', 'Sass', 'Web', 'Example','PHP', 'new', 'Booleans', 'jQuery', 'Overloading', 'return', 'Operators', 
'W3.JS', 'develop', 'today', 'All', 'DOM', 'Abstraction', 'Keywords', 'Files', 'language', 'works', 'abstract', 'W3.CSS', 'Exceptions', 
'course', 'Quizzes', 'correctness', 'End', 'accepted', 'Copyright', 'send', 'Error', 'Programming', 'Test', 'edit', 'Canvas', 'String', 'avoid', 'HOW', 'enum', 'Add', 'Sets', 'Us', 'browser', 'constantly', 'full', '1999-2021', 'AI', 'Next', 'Play', 
'{', 'Color', 'Icon', 'Windows-1252', 'You', 'Front', 'Learning', '.', 'Try', 'Input', 'times', 'result', 'TO', 'Certificates', 'using', 'Handling', 'Parameters', 'Read', 'needed', 'How', 'RegEx', 'used', 'Refsnes', 'class', 'Enums', 'boolean', 'SQL', 'menu', '//www.oracle.com', 'Examples', 'Else', 
'training', 'DTD', 'explanations', 'reviewed', 'While', 'Graphics', '@', 'cookie', '}', 'AngularJS', 'Casting', 'Helping', 'HOME', 'See', 'left', 'easy', 'XSLT', 'ANSI', 'see', 'Class', '4', 'output', 'HTML', 'Main', 'JAVASCRIPT', 'completinga', 'Attributes', 'Kotlin', 'LIKE', 'JavaScript', 'GAME', 'mobile', 
'R', 'use', 'clarifying', 'Browser', 'Home', 'Tag', 'Maps', 'much', 'Git', 'certifiedby', 'Interface', 'listed', 'Get', 'import', 'hesitate', 'Shop', 'try', 'Strings', 'Kickstart', 'privacy', '×', 'site', 'terms', 'Pi', 'us', 'User', 'Constructors', '(', 'optimized', 'many', 'Arrays', 'System.out.println', 'Start', 'Create/Write', 'Top', 'Syntax', 'Rights', 'JSON', 'view', 'About', 'tutorial', 'XQuery', 'might', 'message', 'skills', 'else', 'Chapter', '\ue80b', 'Types', 'web', 'Run', 'Compiler', 'SVG', 'Your', 'w3schools', 'extends', 'desktop', 'content', 'Learn', 'double', 'help', 'Node.js', 'make', 'Polymorphism', '..', 'COLOR', 'part', 'finally', 'started', 'C++', 'Menu', 'File', 'OOP', 'BOOTSTRAP', ']', 'Date', 'Courses', 'reading', 'Thank', 'default', 'MyClass', '#', 'This', 'agree', 'Switch', 'Reserved', 'private', 'AJAX', 'Server', 'Building', 'implements', 'Java', 'Colors', 'With', 'continue', 'PICKER', 'warrant', 'Typing', 'MySQL', 'Threads', 'Data', 'sent', 'References', 'policy', 'Method', 'Methods', 'breaks', 'supplements', 'error', 'Certified', 'Tutorials', ':', 'Tutorial', 'Templates', 'React', 'Forum', 'programming', 'Report', 'XML', 'ASP', '[', 'Support', 'CSS', 'Scope', 'references', ',', 'official', 'JQUERY', 'NumPy', 'Take', 'C', 'args', 'Pandas', 'byte', 'Angular', 'int', 'final', 'e-mail', 'Iterator', 'Statistics', 'Development', 'Schema', 'US', 'read', 'Reference', 'ISO-8859-1', 'For', 'Math', '❯', 'break', 'Exercises', 'short', 'ArrayList', 'Classes/Objects', 'Lambda', 'editor', 'Variables', 'Character', 'XPath', 'Speed', 'HashSet', 'learn', 'Code', 'Matplotlib', 'Two', 'CODE', 'char', 'w3schools.com', 'Editor', 'suggestion', 'Our', 'Packages', 'Classes', 'float', 'Click', 'switch', 'Yourself', 'Symbols', '2021', 'Event', 'Intro', 'ASCII', 'case', 'super', 'Game', 'long', 'Paid', 'oriented', 'Wrapper', 'Go', 'examples', 'Powered', 'SciPy', 'sequence', 'Side', 'API', 'catch', 'Machine', 'Delete', 'Recursion', 'Started', 'errors', '\ue801', 'Google', 'Encapsulation', 'Certificate', 'Raspberry', 'Insert', 'quiz', 'Quiz', 'Numbers', 'career', 'completing', 'learning', 'AppML', 'static', 'go', 'apps', "''", 'Inner', 'Http', 'Security', 'makes', 'Bootstrap', ')', 'package', 'Each', 'Comments', ';'])


print(wordset)

"""
allset = {"DharmikSite":dharmiksite, "SchoolOrCollege":schoolorcollege, "ProgrammingTutorial":programmingtutorial}
#print(keyvaluepairs)

valueset = set()
for i in allset:
    print("keyname = ", i)
    valueset = allset.get(i)
    #print(valueset)
    matches = valueset.intersection(wordset)
    #print(matches)
    lenofmatches = len(matches)
    lenofkeyvaluepair = len(keyvaluepairs)
    print("No of element matches to set =",lenofmatches)
    matchinpercentage = (lenofmatches/lenofkeyvaluepair)*100
    print(matchinpercentage)
#print(wordset)
"""

