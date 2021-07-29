import random
import requests
import lxml.html.clean
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords as sw
import nltk
import matplotlib.pyplot as plt
import json
import pandas as pd
import os



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
  # process the scrap content using NTP after removing all html tags and return wordset and key value pair


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


#Prepare a data set of diffrent diffrent category


dharmiksite=set(["Sarovar","holiest","travel","Pandava","Rameshwar","temple","booking","Dharmic","Heritage","Mandirs","Ghats","Rivers",
"Ghat","River","Ganga","Viswanath","Prakriti","Hindus","Linga","Yatra","TempleKashi","Prasadam","Lord","Teerath","Shiva","Maharani","Baba",
"Donation","shrikashivishwanathtempletrust","Mythology","TEMPLE","Kund","ease-of-darshan","Kund",'Bikaner', 'Shikh', 'Pune','attend',
'teachings', 'monasteries', 'Shivratri', 'certainly', 'Bangalore', 'pervading', 'Rashomoni', 'Char', 'sing', 'Fotolia', 'attract', 
'large', 'popular', 'start', 'hill', 'centuries', 'Trekking', 'Swarn', 'majestic', 'architectural', 'gate', 'Pillar', 'even', 'tasted', 
'Golden', 'time', 'Dhabas', 'nature', 'Some', 'drink', 'forests', 'receive', 'Divine', 'July', 'pages', 'Maharashtra', 'Amritsar', 
'Lawrence', 'paying', 'Tirupati', 'important', 'naturally', 'Balaji', 'Ji', 'said', 'materialistic', 'Legends', 'Spirituality', 'idol', 
'Packages', 'rightly', 'huge', 'survivor', 'Dham', 'Why', 'frequented', 'discrimination', 'District', 'Solitude', 'Works', 'MICE', 
'Uttar',  'Bodhgaya', 'mountains', 'civilization', 'period', 'Omkareshwar', 'North', 'paid', 'Laksmana', 'hall', 'latest',
'experience', 'Sabha', 'Google', 'Blessings', 'traverse', 'built', 'annual', 'Krishna', 'good', 'heavy', 'allows', 'places', 'located', 
'ancient', 'Embrace', 'sanctity', 'offers', 'Watches', 'Don', 'Varanasi', 'Category', 'Sai', 'shrines', 'spiritual', 'enhances', 'every', 
'Moksha', 'combined', 'clean', 'Somnath', 'arduous', 'allow', 'Read', 'South', 'mighty', 'Wildlife', 'excerpt', 'holiday', 'Train', 
'ultimate', 'around', 'No', 'writer', 'get', 'became', 'Sri', 'Q.What', 'Privacy', 'Feast', 'caste', 'dargah', 'Serene', 'Ganga', 'calls', 
'public', 'Shirdi', 'Immaculate', 'praise', 'Tour', 'part', 'pillars', 'Holidays', 'Seize','matches', 'ridge', 'amidst', 'justifies', 
'entering', 'Trains', 'main', 'grown', 'held', 'devotees', 'Ancient', 'travel', 'Only','goddess', 'About', 'Stop', 'Travelling', 
'Sightseeing', 'designs', 'November', 'Beautiful', 'giving', 'Surrender', 'credit', 'Gratitude', 'opens', 'river', 
'Shri', 'matted', 'Rats', 'key', 'Barfani', 'preached', 'heritage', 'Brahmin', 'Significant', 'Rent', 'form', 'alleys', 'ice', 
'drowned', 'ruled', 'ambrosial', 'force', 'takes', 'Sin', 'rich', 'Deccan', 'anything', 'deal', 'Thousands', 'morning', 'Also', 'beckons', 
'Arabian', 'Located', 'practice', 'Way', 'Ramdass', 'listening', 'shiv', 'Interest', 'local', 'cave', 'erotic', 'Who', 'based', 'Stuffed', 
'eternal', 'five', 'storm', 'solo', 'My', 'Hari', 'travelling', 'Holiday', 'Person', 'Apart', 'Dwarkadhish', 'dotted', 'revealed', 
'decent', 'facilities', 'started', 'soak', 'Wheels', 'Borealis', 'useful', 'festival', 'Andaman', 'vibes', 'everything', 'beautiful', 
'virtue', 'One', '99', 'religious', 'Ladakh', 'Experience', 'years', 'word', 'Janmabhoomi', 'stands', 'Odisha', 'temple', 'Nidhi', 
'amounts', 'worship', 'sweet', 'dream', '20', 'adverse', 'Month', 'spent', 'live', 'pyramidal', 'polished', 'dwarkadhish', 'days', 'sitting', 
'Dotted', 'golden', 'killing', 'Assam', 'pilgrimages', 'Kerala', 'means', 'Malaysia', 'memories', 'carved', 'either', 'Mandir/Harmandir', 'popularly', 
'Destinations', 'lot', 'Trudge', 'blaze', 'birthplace', 'Lamayuru', '201301', 'greatest', 'Hills', 'dense', 'Forget', '?', 'Hemkund', 
'belong', 'range', 'pilgrimage', 'undoubtedly', 'wishes', 'conditions', 'Ka', 'colourful', 'God', 'Travel', 'Narmada', 'mesmerizing', 
'drops', 'size', 'Hemis', 'Cave', 'Gurdwara', 'confinement', 'victory', 'media', 'gothic', 'Q.Is', 'Search', 'Punjab', 'blissful', 'settlement', 
'Sab', 'remove', 'result', '15', 'Complete', 'best', 'Special', 'fourth', 'Destination', 'Trikuta', 'disease', 'thrilling', 'surroundings', 'water', 
'content', 'stunned', 'Mannar', 'Venkateswara', 'grand', 'village', 'Winter', 'may','Shakti', 'saint', 'Book', 'Medical', 'Religious', 
'Nainital', 'city', 'Conception', 'celebrated', 'Indian', 'followers', 'Coffee', 'hilltop', 'crowded', 'great', 'redefined', 'cut', 
'taking', 'Jain', 'mesmerized', 'life', 'Singapore', 'Sikh', 'violent', 'Yama-', 'Soul', 'Heritage', 'Most', 'spirituality', 
'remains', 'Pilgrims', 'list', 'amongst', 'western', 'true', 'dolerite', 'Light', 'Kanha', 'images', 'devotees…', 'During', 'heart', 
'seek', 'For', 'Arti', 'overcrowded', 'chariot', 'pair', 'Sikkim', 'Thiksey', 'accompanied', 'journey', 'abode', 'kind', 'ears', 'soul', 'Deserves', 
'Away', 'Thailand', 'architecture', 'From', 'Although', 'Konark', 'whose', 'bringer', 'famed', 'Hotel', 'blog', 'altitude', 'forms', 'Badrinath', 
'Stations', 'February', 'Car', 'called', 'customized', 'ruins', 'Accept', 'horde', 'Yatra', 'innumerable', 'ups', 'colours', 'presides', 'Sector', 
'yatra', 'Narad', 'globe', 'edifice', 'Goddess', 'keeping', 'events', 'affairs', 'Let', 'learn', 'luring', '’', 'pentagonal', 
'could', 'Tickets', 'experts', 'truest', 'bit', 'major', 'Mythological', 'flock', 'code', 'preaches', '‘', 'district', 'Aurora', 
'different', 'Blogs', 'Share', 'Architectural', 'vibe', 'roof', 'Meenakshi', 'hands', 'place', 'Victory', 'Alchi', 'Tirumala', 
'Christian', 'whomsoever', 'Divinity', 'honey', 'contain', 'Guru-', 'Can', 'Nirvana', '1,2020', 'families', 'Goa', 'Jyotirlinga', 
'Jaipur', 'Edu-Tourism', 'Temple', 'destination', 'Vast', 'blogs', 'annually', 'There', 'last', 'India', 'Revel', 'significant', 
'indulgent', 'offering', 'Nagar', 'Puja', 'largely', 'whole', 'pride', 'magnificent', 'I', 'rats', 'hubs', 'clan', 'Source', 'flashes', 
'social', 'Death', 'Odyssey', 'display', 'Temples', 'native', 'Tamil', 'elevate', 'Patnitop', 'Shey', 'Budhha', 'manifold','embrace', 
'Haveli', 'Safeguard', 'centres', 'tips', 'Seva', 'worshipped', 'visit', 'Return', 'Ajmer', 'Mahararashtra', 'lovers', 'Majestic', 
'visiting', 'bountiful', 'accounts', 'green', '72', 'throng', '28th', 'updates', 'Quote', 'hymns', 'spread', 'Situated', 'worth', 
'Narsimhadeva', 'trekking', 'remain', 'Other', 'Health', 'Gir', 'indeed', 'caves', 'something', 'survived', 'monument', 'Kakatiya', 
'details', 'earned', 'October', 'touch', 'tip', 'attention', 'Rishikesh', 'Telangana', 'faiths', '+91-120-4052699', 'Blog', 'Watch', 
'Har', 'created', 'Yourself', 'Ganges', 'Bhavtarini', 'Climb', 'tourmyindia.com', 'truly', 'Thus', 'auspicious', 'trying', 'Cleanse', 
'becomes', 'Amman', 'sheer', 'Palaces', 'weaves', 'Near', 'marvellous', 'incomplete', 'historical', '8', 'enthusiasts', 'bags', 
'Rudreshwara', 'Hooghly', 'together', 'presence', 'tranquil', 'mysterious', 'ago', 'Rameshwaram', 'Mahabodhi', 'Meghna', 'Noida', 'devotion', 
'Baba', 'Characters', '!', 'happens', 'yard', 'Path', 'Unlike', 'That', 'incredible', 'prasadam', 'donation', 'made', 'Haridwar', 'separated', 
'Amarnath', 'Diu', 'art', 'offer', 'riverfront', 'full', 'incarnation', 'epitome', 'favourite', 'Chennai', 'Eyes', 'Power', 'Peda', 
'fame', 'Generic', 'believed', 'exquisite', 'known', 'Himachal', 'scarf', 'magical', 'Vaishno', 'appeared', 'respective', 'Aarti', 
'Lifeline', 'Subhadra', 'state', 'Dip', 'Painful', 'many', 'illumination', 'Company', 'blow', 'rebuked', 'power', 'Durga', 'love',
'Allow', '16,2021', 'Hindu', 'pristine', 'Called', 'lingam', 'Kapil', 'Madurai', 'Nepal', 'day', 'consort', 'finally', 'Sea', 'Portuguese',
'back', 'dipped', 'whirlwind', 'brightness', 'Inarguably', 'nectar', 'behold', 'spired', 'charm', 'Buddha', 'km', 'indelible', 'Receive', 
'Firecrackers', 'Charan', 'Abode', 'head', 'depicts', 'Palakkad', 'cease', 'Feel', 'Dwarka', 'two', 'Legal', 'us', 'Lake', 
'River', 'alley', 'ignore', 'along','Died', 'despite', 'Call', 'world', 'sankranti', 'Gharib', 'united','legacy', 'gratitude', 
'dress', 'Puri', 'crowning', 'Inspired', 'Cruise', 'across', 'decked', 'worldly', 'Pregnant', 'elephants','wish','Sunderban',
'Sanskrit', 'loitering', 'lines', 'sightseeing', 'Bewitching', 'Apr', 'another', 'holiness', 'loveliness', 'customised', 'History', 
'church', 'Posts', 'Fed', 'Shiva', 'Yama', 'Inspirational', 'Facts', 'delightful', 'climatic', 'Laddoo', 'performed', 'Dates', 
'sanctified', 'Recent', 'Bala', 'landscape', 'soothing', 'perfect',  'Popular', 'Virupaksha', 'title', 'This', 'food', 'old', 
'scenic', 'Name', 'rigorous', 'sparkling', 'presiding', 'Maharaja', 'Karnataka', 'grandeur', 'Ahmedabad', 'Rejoice', 'gateway', 
'author', 'reverberates', '300ft', 'imposing', 'trek', 'Social', 'Chhota', 'feeling', 'Jammu', 'discover', 'secret', 'carvings', 
'waits', 'Holiness', 'photography', 'Vishnu.The', 'swords', 'millions', 'collection', 'Raavana', 'Register', 'nonetheless', 'adds', 
'Dubai', 'planning', 'small', 'Hotels', 'Mountain', 'Check', 'drench', 'Thangkas', 'National', 'lake', 'Monsoon', 'Pilgrimage', 
'meandering', 'Life', 'importance', 'attaining', 'Section', 'lies', 'Velankanni', 'rivers', 'Didn', 'glory', 'stones', 'wanderlust', 
'thrice', 'away', 'Chains', 'Peace', 'Homage', '21,2020', '..', 'peek', 'Tibetan', 'piece', 'Dadra', 'Church', 'pursue', 'Corporate', 
'trips', 'September', 'paradise', 'Testimonials', 'level', 'Showered', 'exploring', 'Kingdom', 'evening', 'Pay', 'In', 'divinity', 'lose', 
'Mamleshwar', 'requirement', 'Chandigarh', 'countless', 'Nagaland', 'Tours', 'pray', 'make', 'Find', 'sarovar', 'god', 'forest', 'country', 
'inside', 'Insight', 'faith', 'Panna', 'Whatsapp', 'Sins', 'Tourism', 'hunting', 'hair', '60', 'Lakulisha', 'Nava', 'Hemkunt', 'authentic', 
'shrine', 'Honeymoon', 'engraved', 'follow', 'Take', 'claimed', 'Trending', 'Strength', 'amplifies', 'Park', 'Chariot', 'Best', '7', 'Parvati', 
'essence', 'fascinating', 'City', 'tours', 'earthly', 'style', 'derived', 'posts', '600', 'queer', 'Beach', 'Walk', 'Once', 'nestled', 'Know', 
'numerous', 'thereby', 'Arunachal', 'Grab', 'Talk', 'Sun', 'Kashmir', 'Mathura', 'Pvt', 'round', 'wherever', 'cliche', 'must', 'Janmashtami', 
'Chamoli', 'Pool', 'fulfilling', 'ID', 'several', 'Be', 'Therefore', 'rain', 'Smoking', 'dip', 'Illumination', 'charms', 'Thousand', 'event', 
'Nagapattinam', 'Dakshineswar', 'If', 'blesses', 'Hindus', 'considered', 'learning', 'Humility', 'home', 'Lose', 'image', 'Reckoned', 'June', 
'thus', 'stupas', 'narrow', 'oldest', 'budget', 'first', 'Imbue', 'Lady', 'Visit', 'Lion', 'Pineapple', 'step', 'Kumbh', 'Witness', 'East', 'single',
'twice', 'religion', 'The', 'changed', '50', 'Paramount', 'Horror', 'past', 'side', 'tourism', 'Daman', 'still', 'Supreme', 'Pauri', 'mosques', 
'hours', 'Like', 'activities', 'Good', 'covered', 'Assisi', 'respect', 'inner', 'Bless', 'sins', 'Avail', 'temples', 'going', 'floating', 
'Bandhavgarh', 'Dies', 'urge', 'empyrean', 'Delhi', 'Churches', 'getting', 'money', 'eastern', 'Tips', 'Basilica', 'sculptures', 'structure', 
'Attractions', 'Pondicherry', 'Station', 'List', '60,000', 'tourmyindiadelhi', 'Nawaz', 'MP', 'peace', 'statues', 'swamy', 'existence', 'meditate', 
'yoga', 'Nandi', 'makes', 'Templ', 'Himalaya', 'leads', 'Warangal', 'Home', 'used', 'situated', 'amid', 'shores', 'Karni', 'stay', 'After','Countless', 
'Asked', 'holy', 'essential', 'discovered', 'white', 'number', 'Earthly', 'Devi', 'Makar', 'Images', 'Hyderabad', 'Culture', 'C', 'You…', 'granite', 'often', 
'locations', 'forget', 'Mandap', 'less', 'Instagram', 'Spiritual', 'Sahib', 'April', 'owners', 'Express', 'Mary', 'ambiance', 'longer', 'write', 'holds', 
'cleansing', 'Vishnu', 'tour', 'masterpiece', 'quench', 'Built', 'reasons', 'Disclaimer', 'Boasting', 'propelled', 'Om', 'King', 'Follow', 'brown', 
'repented', 'Media', 'Tourist', 'licenced', 'Rajasthan', 'tolerant', 'Ramanathaswamy', 'All', 'Interesting', 'Ltd', 'creed', 'Top', 'pairs', 'beauty', 
'Harmandir', 'Must', 'diverse', 'centre', 'crowd', 'Elephant', 'Quick', 'Feburaray', 'Enter', 'Main', 'swiftly', 'person', 'Existence', 'Tell', 'Hiring', 
'Prasadam', '81C', 'Famous', 'People', '1855', 'traces', 'Not', 'Chishti', 'childhood', 'keep', 'Gautam', 'closer', 'Information', 'Hill', 'sacred', '6', 
'forever', 'At', 'ideas', 'today', '30', 'would', 'however', 'shall', 'Profile', 'hills', 'Ek', 'Terms', 'divine', 'Themes', 'Today',  'Nativity', 'Our', 
'innovative', 'mind', 'pilgrims', 'cuddled', 'Gurudwaras', '23', 'Plunge', 'Independence', 'south', 'Jim', 'Along', 'nine', 'mystical', 'Gujarat', 
'euphoria', 'gods', 'available', 'finest', 'Guggali', 'vital', 'magnificence', 'invaders', 'snow', 'pleasant', 'Videos', 'Stylish', 'defeated', 'match', 
'Recommended', 'Detailed', 'Always', 'Khwaja', 'history', 'Mahabharata', 'Convent', 'Linga', 'Kaziranga', 'Staircase', 'Resources', 'unmatched',
'Enlightened', 'clothes', 'binging', 'Corbett','Through', 'Highway', 'International', 'set', 'chance', 'pigeons', 'Deals', 'lets', 'Surya',
'afar', 'wear', 'While', 'We', 'miss', 'flowing', 'ask', 'exceptional', 'Bal', 'Radhe', 'weather', 'Believed', 'mentioning', 'mail', 
'Mumbai', 'Serenity', 'try', 'captivates', 'Duration', 'capital', 'attended', 'loiter', 'Q', '*', 'Your', 'indulging', 'courtyard', 
'flickering', 'massive', 'sight', 'Omkar', 'unequalled', 'Fixed', 'Links', 'Stay', 'town', 'Himalayas', 'got', 'Contact', 'prayed',
'Diyas', 'lived', 'emerald', 'rock', 'Cultural', 'new', 'Questions', 'waters', 'genius', 'attracts', 'site', 'packages', 'commemorates',
'delight', 'homage', 'Seshachalam', 'walked', 'gilded', 'Amazing', 'Muslim', 'scenes', 'Get','seekers', 'thirst', 'It', 'Nadu', 
'Ayurveda', 'wheels', 'legend', 'Tiger', 'churches', 'definitely', 'brought', 'contribute', 'Jainism', 'See', 'Bengal', 'concerned', 'Plan',
'Shutterstock', 'Kali', 'Guide', 'Bom', 'including', 'By', 'Published', 'Conditions', 'Sanctity', 'Singh', 'wall', 'Twitter', 'Nights', 
'West', 'Policy', 'shape', 'ritualistically', 'keeps', 'dedicated', 'Lanka', 'Jagannath', 'people', 'January', 'thronged', 'fell', 
'visited', 'Brilliance', 'Purana', 'descendants', 'How', 'Rani', 'consider', 'revered', 'plan', 'without', '4,2020', 'seen', 'March', 
'Mata', 'Teachings', 'driving', 'decently', 'Table', 'Country', 'Package', 'cover', '85', 'Rama', 'blessings', 'big', 'attire', 
'ordinary', 'Adventure', 'According', 'Dharma', 'reincarnated', 'Each', 'tongue', 'allowed', 'Washes', 'making', 'Horizon', 
'structures', 'Universe', 'enthusiast', 'Beware', 'decorum', 'Urs', 'Cup', 'overheard', 'copyright', 'St.', 'always', 'multitude', 
'energetic', 'seeking', 'complex', 'attacks', 'Full', 'Francis', 'times', 'island', 'Vrindavan', 'commendable', 'Extremely', 'Places', 
'Faith', 'Moinuddin', 'land', 'Frequently', 'nothing', 'Kabbas', 'short', 'color', 'enter', 'Buddhist', 'source', 'attraction', 'Us', 
'show', 'granted', 'Ranakpur', 'Air', 'whether', 'Gopal', 'Devotees', 'Email', 'Jesus', 'high', 'Preserving', 'Gate', 'You', 'Pradesh', 
'boasts', '9,2021', 'Bhutan', 'deep', 'Yoga', 'selectors', 'Consciousness', 'directly', 'provide', 'praises', '10,2013', 'Ranthambore', 
'blessed', 'Radha', 'Land', 'banks', 'graceful', 'Kolkata', 'Hampi', 'unparalleled', 'enlightened', '22', 'India-', 'pious', 'yet', 
'Mandir', 'Chardham', 'absolute', 'tourists', 'irrespective', 'Dargah', 'Maalik', 'Alerts', 'Moon', 'expedition', 'sites', 'jyotirlingas', 
'upon', 'Rath', 'packing', 'Sharif', '19,2013', 'Maldives', 'Impeccable', 'stone', 'stole', 'Descriptions', 'long', 'December', 'Sanatan', 
'Hamir', 'Mela', 'Facebook', 'Luxury', 'traveler', 'Explore', 'Saurashtra', 'culture', 'Fulfilled', 'etched', 'famous', 'behave', 
'example', 'affection', 'destinations', 'Arresting', 'Balabhadra', 'year', 'paintings', 'However', 'star', 'indescribable', 'Request', 
'Over', 'Exact', 'Dwadash', 'stepson', 'Dress', 'Lush', 'Weekend', 'Set', 'sons', 'Heart-warming', 'Islamic', 'Departure', 'Since', 
'Pandals', 'immortality', 'bestows', 'Protector', 'deities', 'bath', 'Leh', 'Incredibly', 'trip', 'Bihar', 'includes', 'stuns', 'bliss', 
'pay', 'storeys', 'Imbibe', 'Tribulations', 'August', 'Madhya', 'harmless', 'info', 'edifices', 'adventure', 'Treks', 'Darshan', 'sailor', 
'Wishes', 'Parks', 'Amongst', 'Days', 'expanses',  'comes', 'serenity', 'copyrights', 'needed', 'integral', 'construction', 
'Tigers', 'never', 'Ratna', 'reflection', 'enthralling', 'acquainted', 'Lord', 'Important', 'Town', 'escaped', 'lay', 'flag', 
'Nestled', 'Andhra', 'split', 'Uttarakhand', 'Wedding', 'Seen', 'took', 'States', 'Guidance', 'reached', 'lofty'])



schoolorcollage = set(["STUDENTS","Assistant","designing","Polytechnic","Technology","educational","diploma","department","Eeducation",
"Colleges","Institute","Management","Examination","Computer","Science","Engg","Academics","IT","Chemical","Engineering","Civil",
"Electronics","Electrical","Mechanical","Garment","Applied","Humanities","Courses","Information","Technology","Automobile","Production",
"Admission","Lateral","Training","Alumni","Ragging","Placement","Welfare","Lecture","FACULTY","Toppers","Branch","Rank","Holders","Cyber",
"security","institution","Lab","knowledge",'DharmikSite', 'SchoolOrCollege', 'ProgrammingTutorial','travellingblog','games', 'Code-641', 
'Convocation', 'colleges', 'holy', '5th', 'Play', 'Partners', '13', '24', 'Career', 'Faculties', 'Medical', 'Work', 'AICTE', ';', 'last',
'Affiliation', 'Pedal', 'Us', '2010', 'STUDY', 'Eastern', 'furnished', 'Download', 'practicals', 'Learning', 'Cantt', 'college', 'Gallery', 
'standards', 'Hindustan', 'Hostel', 'AI','Admissions', 'Courses', 'technical', 'February', 'Games', 'State', 'Technololgy', 'Phone', 'distance', 
'Bhartiya', 'KAPPTeC', 'instruments', 'Quick', 'WON', 'AWARDS', 'Lacs', 'activities', 'Ashoka', 'UPSEE-2020', 'great', 'hi-tech', 'There', 'Here',
'Developed', 'NEWS', 'Yr', 'us', 'Privacy', 'Read', 'Rishipattan', 'Anupam', 'Feb', '2nd', 'students','FACULTY', 'Jeans', 'Father', 'Life', 
'Office', 'model', '+91-542-2582255', 'Food', 'buildings', 'AT', 'ETSTM', 'Administration', 'A', 'It', 'Pravashi', 'College', 'lawns', 'COVID-19', 
'comprising', '”', 'delicious', 'bad', 'Links', 'Station', 'Classrooms', '2018', 'You', 'central', 'Trends', 'Sahara', 'held', 'Regarding', 'placed',
'National', 'Recognition', 'Rizwan', 'interior', 'Ujala', 'Sports', 'labs', '3rd', 'Divas', '2019', 'For', 'international', 'Engineering','green', 
'Competition', 'Machine', 'Find', 'Year', 'Filter', 'meant', 'ASHOKA', 'Study', 'Technical', 'Only', 'available', 'Facebook', 'YEARS', 'Very', 
'modern', 'Want', 'EXCELLENCE', 'extremely', 'Paharia', 'Redressal', '&', 'Registration', 'companies', 'Sarnath', 'enlightenment', 'reflects', 
'library', 'heart', "'s", 'Air', 'technology', 'We', 'senior', 'yoga', 'outbreak', 'dotted', '-', 'More', 'Amar', 'Dashboard', 'Reserved', 'News', 
'big', 'Conference', 'BRAND', 'started', 'hygiene', '%', 'Pharmacy', 'Education', 'canteen', 'still', 'hire', 'Placement', 'got', '1.5', 'using', 
'Technology', 'Email', 'View', 'conscience', 'workshops', 'subject', 'Institute','nice', 'Schedule', 'Farewell-18','Abhyuday-20', 'Excellence', 
'ground', 'Railway', 'Award', 'Campus', 'food', 'halls', 'practical', '2017', 'Postgraduate', 'Library', 'Many', 'Training', 'Buddha', 'located', 
'existence','Abhyuday', '27', '?', 'FDP', '25',  'GRS', 'Scholarship', 'The', 'acres', 'attractive', 'near', 'Letter', 
'Gun', 'good', 'Our', 'Also', 'Poster', 'Annual', 'World', 'necessary', 'came', 'going', 'Learn', 'distribution', 'visit', '26', 'U.P', 'Intelligence', 
'city', 'Extension', 'Memories', 'Rohit', 'To', 'call', 'keep', 'Device', 'poor', 'Fax', 'Monday', 'quality', 'Rights', 'Saturday', 'ETSTM-2019', 
'Generator','campus', 'training', 'new', 'race', 'ashokainstitute.com', 'art', 'laboratories', 'Chauraha', 'ERP', 'facilities', "Abhyuday'20", 
'Programmes', 'PCI', '5PM', 'AKTU', 'Site', 'Media', 'package', 'WORLD', 'Created', 'Kashivarta', 'Course', 'best', 'Pvt', 'get', 'DUBAI-2016', 
'infrastructure', 'memories', 'Lord', 'Best', 'day', '3.5', 'cafeteria', 'Contact', 'Simran', 'Selection', 'OF', '20-21', 'Position', 
'Python', 'Cafeteria', 'Copyright', 'every', 'Management', 'Login', 'Most', 'Washing', 'place', 'Student', 'institute', 'camp', '4th', 'One', 'All', 
'Anti', 'presented', 'Pollution', 'Science', 'Undergraduate', 'prize', 'Testimonials', 'System', 'span', 'Project', 'Policy', 'facility', '70', 'Online', 
'SUMMIT', 'Follow','year', 'workshop', 'Notice', 'Map', 'Aikido', 'Certificate', 'management', 'eastern', 'placement', 'Separate','lush', 'About', 
'Varanasi-221007', 'seminar', 'Varanasi', 'well', '9AM', 'App', 'hands','Home','Call', 'Address','Electricity','km', 'UP', 'INDIA', 'Classes', 'Grievance',
'named', 'Rape', 'awarded', 'info', 'PLACEMENT', 'US', 'Anjali', 'Subscribe', 'due', 'Banarasi','books', 'Kalam', 'Emerging', 'Promising', 'Newsletter', 
'Procedure', 'Marketed', 'MHRD', 'Events','Request', 'corner', 'Strength', 'Lodging', 'Results', 'And', 'e-Prac', 'Duplicate', 'Care', 'Sample', 'Rapid', 
'Award', 'Absent', 'Public', ')', 'Directions', 'Assisting', 'Online', 'Latest', 'Awards', 'OSAMS', 'Refund', 'FAQs/Guidelines/Manual', 'Register', 
'ACADEMIC', 'Statistics', 'data', 'Sangathan', 'Day', 'Minor', 'Transfer', 'Grievances', 'AWARDS', 'Books', 'Teacher', 'FAQs', 'Interventions', 'Locator', 
'Quality', 'Important', 'Issuance', 'checking', 'Currently', 'Grievance', 'E-Books', 'Monitoring', 'Policy', 'Schools/Students', 'name/Logo', 'Alerting', 
'Uploading', 'Rules', 'Practices', 'In', 'last', 'admission', 'India', 'RESULT', 'National', 'Digital', 'Initiative', 'Marks', 'Callers', 'Higher', 'School', 
'Boosting', 'CVL', 'Counselling', 'applications', 'marks-regarding', 'Preventive', 'PRINCIPALS', 'Organisations', 'Affiliated', 'ELIGIBILITY', 'International', 
'Database', 'TEST', 'Safe', 'Syllabus', 'SYSTEM', 'Forms', 'Making', 'Your', 'Material', 'EXAMINATION', 'Notice', 'Annual', 'Scholarships', 'Open', 'various', 
'Guidelines', 'Headings', 'Parents', '(', 'Assessment', 'Brochure', 'Click', 'Candidates', 'Inclusion', 'E-Trainings', 'Answers', 'Admission', 'Cases', 'Number', 
'AND', 'Teachers', 'A', 'Legal', 'Extension', 'FIT', 'Examination', 'HPE', 'Vision', 'Games', 'Computation', 'Curriculum', 'verification', 'Information', 'Support', 
'Classes-X', 'SERVICES', 'Academics', 'Manual', 'Pass', '2022-23', 'COMPREHENSIVE', 'PORTAL', 'launching', 'Next', 'List', 'Transmission', 'Workshops', 'Operational', 
'Registration/LOC', 'Agency', 'Principals', 'New', 'Refraining', 'Capabilities', 'PUBLIC', 'Technology', 'Skill', 'Fee', '01/07/2021', 'Taken', 'Subject', 'Class', 
'Calendar', 'Certificate', 'Search', 'Types', 'date', 'Here', 'Coronavirus', 'System', 'JOINT', 'News/Frivolous', 'Self',  'X', 'Facilities', 'DIKSHA', 'Grading', 
'uploading', '&', 'Purchase', 'DOCUMENT', 'Questions', 'COVID', 'main', 'Direct', 'Section', 'Rumours', 'Combinations', 'A-', 'viz.', 'Center', 'Question', 'CUM', 
'Student', 'Tenders', 'Board', 'Stakeholders', 'KYA', 'Locker', 'Scheme', 'Social', 'Central', 'XII', 'Class-XI', 'Manuals', 'Immunity', 'Each', 'Recruitments', 
'Reducing', 'Activities', 'Compendium', 'Applications', 'Increase', 'without', 'Letter', 'Judgements', 'Navodaya', 'Mapping', 'Disease', 'Written', 'CTET', 
'Protocol', 'Schools', 'RESULTS', 'Resources', 'Class-X', 'Alert', 'Tender', '–', 'Personnel', 'Manjusha', 'Communication', '-', 'Clause-14', 'TEACHERS', 
'For', 'Answer', 'Unauthorized', 'Addition', 'Helpline', 'Result', 'Papers', 'Framework', 'IT', 'Harkara', 'Cyber', 'CBSE', 'Students-regarding', 
'E-Resources', 'Institute', '23/06/2021', 'etc', 'Unscrupulous', 'Management', 'GIS', 'Know', 'Shortage', 'Sister', 'Single', 'Previous', 'Students', 
'Procedures', 'Exhibitions', 'Notification', 'Two', 'Publications', 'Professional', 'Mandatory', '19', 'III', 'Marking', 'Admn.II', 'NSDL', 'Notices', 
'Academic', 'Chairman', 'Government', "'", 'timeline', 'Training', '|', 'session', 'Other', 'affiliation', 'Sanctioned', 'Offered', 'Verification', 
'Institutions', 'UMANG', 'Depository', 'Testing', 'Press', 'Address', 'Attendance', 'Portals', 'Distancing', 'Ayush', 'Apprenticeship', 'Education', 
'DUPLICATE', 'content', 'OECMS', 'CDSL', 'Years', 'SARAS', 'Qualification', 'Fees', 'Name', 'Misleading', 'Reg', 'Rajbhasha', 'Check', 'Asked', 'Wing', 'Boards', 
'Schooling', 'Migration', 'Correction', 'NCERT', 'RTI',  'Council', 'Portal', 'Conduct', '30/06/2021', 'Advisory', 'Affiliation', 'Finance', 'use', 'Samiti', 
'MHRD', 'Vidyalaya', 'OASIS', 'Plan', '12th', 'Novel', 'Schemes', '@', 'Tabulation', 'Beware', 'Administration', 'Board-', 'Various', 'Follow', 'Comprehensive', 
'Last', 'External', 'SWC', '2021', 'Secondary', 'Exam', 'NDML', 'Details', 'Charter', 'Accounts', 'Admin', 'Safety', 'Document', 'Rehabilitation', 'taken', 
'Competitions', 'categories', 'Kendriya', 'Videos', 'facility', 'Principal', 'Links', 'Stakeholder', 'Particulars', 'Automation', 'NATIONAL', 'IX-X', 'Regard', 
'TABULATION', 'logo', 'regarding', 'Voters', 'Implementations', 'Innovative', 'Cell', 'Release', 'XI-XII', 'Policies', 'Recruitment', 'Subjects', 'PPT', 'COEs', 'Media', 
'Marksheet', 'Re-Engineered', 'Corner', 'E-Learning', 'Registered', 'Podcasts', 'Frequently', 'Resources/Learning', 'Control', 'ENTRANCE','Ethics', 'Ministry','Ventures', 
'Frivolous','Bye-laws', 'Tests', 'Entrance', 'Expectations', 'Extent', 'Marksheet/Pass', 'Against','Model', 'e-Pareeksha', 'Examinations',
'Courses', 'Accessibility', 'Change', 'Video', 'Service', 'Competency', 'Special', 'FOR', 'status', 'Recommended', 'Citizen', 'Digi-locker', 
'CLASS-XII',  'Unit', '+2', 'Stay', 'Documents', 'Window', 'E-pareeksha', 'About', 'Procedure', 'Mark', 'Class-XII', 'CWSN', 'Implementation', 
'Anomaly', 'Focus', 'Services', 'Awareness', 'Directives', 'Avoid', 'Fashion', 'Bench', 'Exams', 'Helpdesk', 'Moderation', 'PWD', 'Studies', 'Circulars', 'Certificate/Migration', 
'Initiatives', 'Parinam', 'Limited', 'Status', 'Additional','A+', 'Letters', 'Creating','Pending', 'SEMINAR', 'Important', 'power', 'Nucleus', 'boundaries', 'Khan', 'Puru', 
'LABVIEW', 'Western', 'Anas', 'industrial', 'Campus', 'BYJU', 'Contact', 'DEFAULTERS-', 'Adani', 'IRJET', 'Informatica','Scholarship', 'Garima', 'occasions', 'received', 'knowledge',
'concluded', 'COMMUNICATION', 'Vashisht', 'professional', 'reductions', 'CELL','untimely', 'Kotak', 'industries', 'SRM', "Student's", 'India', 'This', 'Svayam', 
'Memberships', 'Challenge', 'Parents', 'modules', 'secure', 'Civil', 'Placement', 'Mathematics', 'Science', 'powered', 'Professional','Vinamra', 'Policies', 'M.B.A', 'team', 'REVISED', 'Conditioning',
'series', 'participation', '17', '03-Mar-20', 'comfortable', 'Admission', 'Global','REIMBURSEMENT', 'give', 'thereby', 'University', 'Sessional', 'Committee', 'Technical', 'Fees', 'Sep',
'Faculty', 'Internship', 'CARD', 'DAY','Instructions','Papers', 'Exams', 'Conduction', 'Checklist', 'WALK', 'Almirah', '09', '25-Feb-20', 'Training', 'Central', 'Administrative', 
'Meditation', 'situation', 'ME', 'Yr.', 'Aspirants', 'COP', 'Education', 'effectively', 'affiliated', 'event', 'Gym', 'Week', '10-Feb-20', 'enhance', '2020-2021', 'distinction', 
'provide', 'provided', 'developed', 'compared', 'pretty', '27th', 'MERIT', 'admitted', 'RCM', 'IT', 'AND', 'Webs', 'supporting', '08', 'value-based', 'Social', 'Corporate', 'With', 
'Eastern', 'Night', '98.3', 'Forcepoint', 'COMMENCEMENT', 'best', '&', 'Odd', 'INSTALLMENT', 'KI', 'Bank', 'Royal','ARMY', 'Kr', 'Nishant', 'Shri', 'FILLING', 'Colleges','Bajaj', 'Academics', 
'Result', 'GEN', 'Courses', 'Institue', 'Mohammad', 'weather', 'Engineering', 'Env', 'ADMITTED', 'Nov', 'gets', 'Companies', 'Routes', 'Library', 'practical','ONCOMPUTING', 'HCL','AICTE','App',
'air', 'Tiwariganj', 'many', 'M.Tech', 'COMMITTEE', 'commendable', '©', 'Kartik', 'preaching', 'Affidavit', 'make', 'Software', 'Zenus', 'CLASSES', 'Only', 'Uploading', 'Electronics', 'ASSISTANT', 
'Innovation', 'Summer', 'SESSION', 'Ajendra', 'oneself', 'Bravehearts', 'F3', 'Birla', 'CTC', 'Mirchi', 'Apco', 'March', 'Medical', 'curriculum', 'training', 'Amazon', 'Gallery', 'Congratulations', 
'companies', 'cultural', 'Verma','supportive', 'encouraged', 'Seminar', 'steria', 'Invention', 'Process', 'leading','guiding', 'Insurance', 'always','Instruments', 'ANTI', 'witnessed', 
'Srivastava', 'provides', 'Pre', 'grab', 'enhancement', 'GR', 'Air', 'programmes', 'Honouring', 'Daffodil', 'aptitude', 'Adoption', 'passenger', 'festival', 'ever','Life', 'December', 
'Certybox', 'Copyright', 'guided', 'Passing','zero', 'batch', '000', 'Project', 'Of', 'Department', 'Anti', 'Lido', 'EXAMINATION', 'Applied', 'Student', 'form', 'Asahi', 
'institutional', 'journey', 'puts', 'TCS', 'Mphasis', 'efficient', 'Excellence', 'BEEAAR', 'FEES', 'VVDN', 'schedule', 'conference', 'Metacube', 'First', 'employability', 'ratio', 
'fuel', 'CATEGORY', 'Documents', 'came', 'tour', '07', 'RAGGING', 'Grobots', 'Hike', 'Harassment', '``', 'REBATE', 'time', 'Infoware', 'Accounts', 'Beyond', 'Counselling',
'RAGGING-SURVEILLANCE', 'Edugorilla', 'RCE-074', 'Webkul', 'MBA/MCA', 'Tommy', 'Emeis', 'AMCAT', 'Students', 'Clubs', 'News', 'E-', 'NIIT', 'colleges', "Byju's", 'Singh', 
'EXTENSION', 'singer', 'emissions', 'Wooded', 'Useful', 'PLACEMENT', 'Lucknow', 'Holders', 'STUDENTS', 'awareness', 'System', 'go', 'Akash', 'Paper', 'cleared','literature', 
'international', 'understand', 'HOSTEL-BUS', 'Alumni', 'Revised', 'scholarship', 'HelpLine:757', 'push', 'Holidays', 'Aanlogy', 'holistic', 'Go-Kart', 'IC', 'Calendar', 'huge', 
'Matric', '26', 'session', 'Anglo','gratitude', 'new.Events', 'Placed', 'Departments', 'Mahotsav', 'CHARGE', 'program', 'THIRD', 'Touch', 'levels', 'STAR', 'Structure', 
'post-graduation', 'Srishti', 'student', 'Kavach', 'Group', 'life', 'staffs', 'years', 'Offered', 'Researchers', 'programme', 'Pre-End', 'security', 'NEWLY', 'Vansh', 
'gave', 'UP', 'sir', 'regarding','placed', 'VISITS', 'Chhatra', 'Matrix', 'learn', 'crack', 'Us', 'stand', 'Sciences','Windmöller', 'across', 'fact', 'Coforge',
'Pended', 'Management', 'Postponement', 'Mechanical','practices', 'Belongings', 'Procedure', 'Intermesh', 'system', 'Trends', 'POST', 'consumption', 'Abdul', 'REGARDING', 
'installment', 'promptly', 'Thoughtworks', "''", 'Capgemini', 'Assistance', 'Postpone', 'Jan', 'Profiling', 'Health', 'Shukla', 'efforts', 'Construction', 
'I.C', 'Swayam', 'Secretary', '28th', 'Members', 'Prulife', 'payment', 'KNC302', 'Ltd.', 'Senate', 'platform', 'Guidelines', 'ALUMNI', 'appreciation', 'Registration', 
'FUN', 'Reliance', 'currently', 'Daikin', 'necessary', 'every', 'Novelvox', 'CAPGEMINI', 'Season', 'Upcoming', 'fun', 'faculty', 'INDIA', 'Government', 'pre-placement', 
'organized', 'Even', 'IEEE', '04-Feb-20', 'preparatory', 'Classes', 'Technologies', 'find', 'academics', 'Drives', 'Patel', 'Vishwakarma', 'Updates', 'offered','Collection', 
'conferences', 'Ashish',  'Additional', 'Border', 'wise', 'effort', 'getting', 'Google', 'sincere', 'B.Tech/M.Tech', 'high','exposure', 'Activity', '10', 'Recruiters', 
'desirous', 'PROCTORIAL', 'UPDATE', 'Meets', 'wonderful', 'Gantavya', 'Marks', 'sincerely', 'better', 'Centre', 'Physics', 'COLLECTION', 'drive', 'Cognizant', 'Unthinkable', 
'helped', 'shipping', 'thankful', 'two', 'Transport', 'providing', 'Payment', 'graced', 'Enviro', 'newly', 'grateful', 'course', 'CE', "Recruiter's", 'Conequip', 'Defense', 
'Specially', 'Test', 'classes', 'B.TECH', 'existing',  'BCA', 'Phronesis', 'N', 'Using', 'SRDT', 'Reliable', 'Fee', 'DRIVE', 'Star', 'Communication', 'PINCAP', 'Donation', 
'Paints', 'STUDENT', 'placement', 'Divyank', 'OFFER', 'skills', 'Ramswaroop', 'chance','GVK', 'Addition', 'opportunities', 'Pakhwara', 'Super', 'design', 'Defaulters',
'Mock', 'facility', 'HDFC', 'Viva/', 'Yards', 'kumar', 'FOR', 'Pvt', 'Graphics', 'Contributions','Merit', 'challenges', 'ADJUSTMENT', 'Course', 'Mybreakfix', 'coding', 'ODD', 
'Infinet', 'Quiz', 'environment', 'Slip', 'Audit', 'rocked', 'Shivam', 'rise', 'EC', 'availing', 'Cell', 'adequate', 'full', 'amazing', 'TECHNOLOGIES', 'Village', 'Open',
'Hostels', 'upto', 'Demo', 'FEE', 'Young', 'TECHNOLOGY', 'Apart', 'COGNIZANT', 'energy', 'less', 'project', 'The', 'E-Consortium', 'FORM', 'Induction', 'Constructions', 'dt', 'Fee-', 
'Research', '3rd', 'NCC', 'Concession', 'True', 'PTC', 'MOBCODER', 'Ginger', 'Power', 'parent', 'Torrent', 'Aditya', 'Pyrolytic', 'Samarth', 'Conclave', 'Chapters', 
'members', 'Solution', 'PROGRAM', 'National', 'Smokeless', 'NOTICE-GENERAL', 'Date', 'Mandatory', 'MEDALS', 'exam', 'soft', 'fee', 'PROGRAMME', 'EVEN', 'atmosphere','Regular', 
'Organization', 'selected', 'clubs', 'Stove', 'stoves', 'Authentications', 'Cloud', 'Complete', 'Dial', 'ACM', 'Abhivyakti', 'Report', 'held', 'helpful', 'Extension', 'Axis', 
'OF', 'Engineers','overall', 'Steel', 'kart', 'admissions', 'bikers', 'gives', 'bus', 'Berger', 'step', 'NOMINATION', 'term', 'part', 'Admissions', 'Reminder-3', 
'Recruitment', 'INDIAN', 'become', 'Placements', 'MINORITY', 'guide', 'interviews', 'Infosys', 'Relaxation/', 'Canteen', 'ensuring', 'KSolves', 
'Progress', 'EMRI', 'Partners', 'Brown', 'Administration', 'lpa', 'Alam', 'development', 'During', 'ICT', 'Hölscher', 'Extramarks', 
'Extended', 'MCA', 'Anti-Sexual', 'achieved', 'Mr.', 'Apply', 'Unicode', 'department','goes', 'helps', 'LIST', 'Dignitaries', 
'Application', 'WARRIORS', 'Finance', 'Fortress', 'success', 'Local', 'Details', 'End', 'Resource', 'ALL', 'IBM', 'Policy', 'Facility', 'Submission', 
'conclave', 'Grievance', 'SRMCEM', 'Post', 'conduct', 'JULY', 'SAP', 'Brochure', 'Mess', 'Academic', 'Functionaries', 'gas', 'NPTEL', 'V', 'Gupta', 
'Infratech', 'Cedcoss', 'confidently', 'USA', 'imparting', 'SCHOLARSHIP', 'modern', 'group', '15-16', 'IN', 'Square', 'Ramky', 'Chart', 'Hubs', 'awards', 'reserved', 
'25-27', 'Messages', 'Tech', 'INTERNATIONAL', 'Blood', 'institutes', 'us', 'develop', 'Btech', 'June','Special', 'organisations', 'expectations', 'Sopra', 'something', 'ROOM', 
'pre', 'Notices', 'International', 'Program', 'Login', 'Camp', 'officers', 'Kuldeep', 'Conferences', 'FIRST', 'Analysis', 'Sem', 'Maintaining',  'Computer', 'Hilfiger', 
'ATTENTION', 'END', 'Ericsson', 'Tour', 'Commencement', 'ICICI','online', 'BBA', 'great', 'Industries', 'Enfiled', 'URGENT', 'Fortune', 'Mahindra', 'Arpan', 'Route', 'May', 
'Spardha', 'Redressal', 'Out', 'right', 'filling', 'Notice', 'learning', 'AKTU','Branch', 'Practical/', 'recognized','INTERVIEW', 'srmcem.ac.in', 'Paytm', 'monitoring', 
'List', 'etc', 'Testimonials', 'K', 'good', 'M.C.A', 'EXAM', 'ThoughtWorks','Humanities', 'E-Resources', 'IndiaMart','hand', 'Outreach', 'know', 'Anshul', 'insightfully',
'stroke', 'Repository', 'communication','low', 'front', 'Staff', 'Calender', 'Smart', 'activities', 'Alpha', 'Uttar', 'opportunity', 'Memorial', 'Nomination', 
'Information','Bus', 'Dr.', 'proves', 'practice', 'Collabera', 'Eckovation', 'Last', 'sessions', 'Focus', 'Exam', 'Now', 'NSS', 'College', 'R1', 'quality', 'CONTROL', 'weight', 
'NOTICE', 'iB', 'SOFTPRO', 'Pradesh', 'Gahlot', 'apart', 'Motifespace','Solutions', 'sure', 'Related', 'final', 'Papon','Optimus', 'Johnson', 'Online',
'Budget', 'Prism', 'believe', 'CoronaVirus', 'AUTOMATION', 'Newsletters', 'GENERAL', 'Reports', 'Mission', 'crucial', 'really', 'business', 'culture', 'My', 'Chemistry', 'Chairman', 
'students', 'Top', 'Essell', 'INDUCTION', 'Aftab', 'Links', 'MBA', 'CONFERENCE', 'Ragging', 'Programming', 'makes', 'Bollywood', 'reached', 'COVID', 'education', 'Organizational', 
'excellent', 'Sports', 'Best', '50', 'vain', 'towards', 'Elective', 'targets', 'Shrivastava', '/Python', 'NS', 'units', 'Director', 'Functional', 'Ltd', 'OBC', 'MEET', 
'Session', 'Vision', 'Regarding', 'Hostelers', 'Financial', 'paid', 'Feb', 'e-Portal', 'helping', 'Chip', 'Kalam', 'Learning', 'published', 'ADMIT', 'academic', 'got', 'Mumbai', 
'Sharma', 'Downloads', 'may', 'Logic', 'Wipro', 'IQAC', 'Careers', 'Antiragging', 'Change', 'Enquiry', 'More', 'Evaluation', 'experience', 'Demographic', 
'platforms', 'Autowheel', 'PeopleSoft', 'Road', 'GeeksforGeeks', 'encourage', 'death', 'Infracon', 'Entrepreneurship', 'Electrical', 'technical', 'placements', 'Innovations',
'Schedule', 'director', 'MDP', '11', 'conditioned', 'E-Repository', '29-31', 'performance', 'college', 'Chapter', 'Affairs', 'excitement', 'Oracle', 'Ayush', 'Classroom', 'ON', 
'In', 'Get', 'company', 'Binz', 'Executive', 'ABHIVYAKTI', 'day', 'Van', 'Technology', 'Semester', 'THE', 'SRMGPC', 'Generation', 'Swacchata', 'concepts', 'Dear', 'Here', 
'Mental', 'Tata', 'MBA-I', 'TEAMS', 'DATE', 'Anti-Ragging', 'CS', 'Khare', 'B.Tech.', 'examination','B.Tech', 'CSR', 'interview',  'in-depth', 'cases', 'Approvals', 'Reminder', 
'U.P', 'cell', 'Attention', 'Examination', 'Triveni', 'Schedules', 'Infraprojects', 'SEMESTER', 'Ranking', 'Radio', 'CoCubes', 'Filling', 'INDUSTRIAL', 'Pvt.Ltd', 'Bharat', 
'conducted', 'place', 'Events', 'Yash', 'Singsys', 'Newly', '12', 'Smartprix', 'All', 'RANKING','Annual', 'HR', 'HALLS', 'Final', 'Content', 'Systematics','motorbikes', 'IIT', 
'Meritorious', 'certify', 'EE', 'various', 'Gainsight', 'CONGRATULATIONS', 'Engg', 'KNC301', 'Achievements', 'M.TechClick', 'Disclosure', 'Guest', 'lore', '8th', 'RESEARCH',
'reputed', 'top', 'Facilities', 'zones', 'A.P.J', 'Human', 'Travel', 'Notice-Fee-64', 'SC', 'internships', 'world', 'PNS', 'February', 'BOARD-DISCIPLINARY', 'Ergo', 'Eligibility', 'Sukriti',])



programmingtutorial = set(['Keylogger', 'Features', 'IndexingNumpy', 'Notes', 'cutting', 'experience', 'Using', 'AnalysisData', 'value', 
'WiproCrack', 'TCS', 'SetsPython', 'bit_length', 'askquestion', 'PythonPrecision', 'ConceptsPython3', 'Birthday', 'Chatting', 'Geek',
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
'SortMongoDB', 'PythonCollections.UserList', 'QuizzesGATEGATE', 'PythonPython-Tkinter', 'Series', 'DesignDigital', 
'HandlingException', 'OpenCVPython', 'install', 'Learn', 'PythonDefaultdict', 'TutorialSelenium', 'examples.Below', 'PacedStart',
'Dropbox', 'Wikipedia', '*', 'FindPython', 'While', 'Toplevel', 'online', 'formating', 'KivyGridLayouts', 'operations', 'Calculator100', 
'PythonMake', 'Pradesh', 'booleanTernary', 'Gates', 'effectivelyPython', 'pythonC/C++', 'JobsCome', 'suited', 'PyTorchPython', 'Tracker',
'New', 'APIFetching', 'Processing', 're.search', 'OperatorsData', 'Netflix', 'GATE', 'MongoDB', 'feedback', 'user', 'Please', 
'Multi-threading', 'variablePrivate', 'Original', 'Checkbutton', 'PageLayout', 'Windows', 'Filter', 'Order', 'Instagram', 'TuplesPython', 
'functionsPython', 'MySQLPython', 'migrationNews', 'PythonCollections.UserDict', 'Searching', 'Maths', 'ModelsDjango', 'object',  'kwargsPython',
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
'provides', 'ProgrammingDivide', 'lexicographical', 'Object', 'SeleniumSelenium', 'C',  'ArraysControl', 'PythonPolymorphism', 'Examples', 
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
'course', 'Quizzes', 'correctness', 'End', 'accepted', 'Copyright', 'send', 'Error', 'Programming', 'Test', 'edit', 'Canvas', 'String',
'avoid', 'HOW', 'enum', 'Add', 'Sets', 'Us', 'browser', 'constantly', 'full', '1999-2021', 'AI', 'Next', 'Play', 
'Color', 'Icon', 'Windows-1252', 'You', 'Front', 'Learning',  'Try', 'Input', 'times', 'result', 'TO', 'Certificates', 
'using', 'Handling', 'Parameters', 'Read', 'needed', 'How', 'RegEx', 'used', 'Refsnes', 'class', 'Enums', 'boolean', 'SQL', 
'menu', 'Examples', 'Else', 'training', 'DTD', 'explanations', 'reviewed', 'While', 'Graphics',  'cookie', 'AngularJS', 'Casting', 
'Helping', 'HOME', 'See', 'left', 'easy', 'XSLT', 'ANSI', 'see', 'Class', '4', 'output', 'HTML', 'Main', 'JAVASCRIPT', 'completinga', 
'Attributes', 'Kotlin', 'LIKE', 'JavaScript', 'GAME', 'mobile','R', 'use', 'clarifying', 'Browser', 'Home', 'Tag', 'Maps', 'much', 
'Git', 'certifiedby', 'Interface', 'listed', 'Get', 'import', 'hesitate', 'Shop', 'try', 'Strings', 'Kickstart','site', 'terms', 
'Pi', 'us', 'User', 'Constructors','optimized', 'many', 'Arrays', 'System.out.println', 'Start', 'Create/Write', 'Top', 'Syntax', 
'Rights', 'JSON', 'view', 'About', 'tutorial', 'XQuery', 'might', 'message', 'skills', 'else', 'Chapter', 'Types', 'web', 'Run', 
'Compiler', 'SVG', 'Your', 'w3schools', 'extends', 'desktop', 'content', 'Learn', 'double', 'help', 'Node.js', 'make', 'Polymorphism',
'COLOR', 'part', 'finally', 'started', 'C++', 'Menu', 'File', 'OOP', 'BOOTSTRAP', 'Date', 'Courses', 'reading', 'Thank', 'default', 
'MyClass', '#', 'This', 'agree', 'Switch', 'Reserved', 'private', 'AJAX', 'Server', 'Building', 'implements', 'Java', 'Colors', 'With',
'continue', 'PICKER', 'warrant', 'Typing', 'MySQL', 'Threads', 'Data', 'sent', 'References', 'policy', 'Method', 'Methods', 'breaks', 
'supplements', 'error', 'Certified', 'Tutorials',  'Tutorial', 'Templates', 'React', 'Forum', 'programming', 'Report', 'XML', 'ASP',
'[', 'Support', 'CSS', 'Scope', 'references',  'official', 'JQUERY', 'NumPy', 'Take', 'C', 'args', 'Pandas', 'byte', 'Angular', 
'int', 'final', 'e-mail', 'Iterator', 'Statistics', 'Development', 'Schema', 'US', 'read', 'Reference', 'ISO-8859-1', 'For', 'Math', '❯',
'break', 'Exercises', 'short', 'ArrayList', 'Classes/Objects', 'Lambda', 'editor', 'Variables', 'Character', 'XPath', 'Speed', 
'HashSet', 'learn', 'Code', 'Matplotlib', 'Two', 'CODE', 'char', 'w3schools.com', 'Editor', 'suggestion', 'Our', 'Packages', 'Classes', 
'float', 'Click', 'switch', 'Yourself', 'Symbols', 'Event', 'Intro', 'ASCII', 'case', 'super', 'Game', 'long', 'Paid', 
'oriented', 'Wrapper', 'Go', 'examples', 'Powered', 'SciPy', 'sequence', 'Side', 'API', 'catch', 'Machine', 'Delete', 'Recursion', 
'Started', 'errors', 'Google', 'Encapsulation', 'Certificate', 'Raspberry', 'Insert', 'quiz', 'Quiz', 'Numbers', 'career', 'completing', 
'learning', 'AppML', 'static', 'go', 'apps', 'Inner', 'Http', 'Security', 'makes', 'Bootstrap', ')', 'package', 'Each', 'Comments', ';'])


travellingblog = set(['Mumbai', 'start', 'Weekends', 'winter', 'Nature', 'IndiaTravelBlog', 'Create', 'Expedia', 'Clase', 'escalas', 
'suiting', 'Go', 'Indian', 'still', 'bank', 'nation', 'Visit', 'Friday', 'Stations', 'Your', 'cities', 'checking', 'Best', 'Hours', 
'landscape', 'Rebecca', 'Malaysia', 'How', 'Vyjay', 'Cities', 'Top', 'Budget', 'special', 'making', 'turn', 'feel', 
'Events', 'world', 'Ganga', 'many', '15/09/2017', 'river', 'must-visit', 'called', 'food', 'Kerala', 'Nadu', 'Pick', 'Shop', 'Favourite',
'Urmi', 'Good', 'ActivitiesCulturalCultureFestivals', 'Oceania', 'Corrige', 'part', '02420', 'Getaway', 'every', 'sight', 'shopping', 
'EventsIndia', 'check', 'India', 'nice', 'ghats', 'Holiday', '–', 'display', 'City', 'Culture', 'Located', 'Ginni', 'Itinerary', 
'January', 'heritage', 'Dave', 'Mark', 'dates', 'チェックアウト', 'Tourist', 'find', 'blog', 'chaotic', 'sets', '8', 'Ltd', 'Arts', 
'state', 'Calendar', 'universal', 'Book', 'guide', 'discover', 'location', 'Origin', 'Monsoon', 'capital', 'Tips', 'Travel','sorted', 
'offers', 'World', 'Support', 'National', 'need', '&', 'Tourism', 'indian', 'around', 'Bengaluru', 'travelling','Sin', 'rake', 
'Asia', 'airport', 'Have', 'Season',  'Hotels', 'view', 'Pte', 'Press', 'Destinations', 'flavours','Guide','Constitution',
'Forts', 'Account', 'overgrown', 'Pakistan','Blog', 'Goa', 'brings', 'Beaches', 'Plan', 'Ooty', 'experiencing','But', 'One', 
'Andra', 'top', 'sounds', 'yet', '07/08/2018', 'visits', 'tagged',  'Customer', 'time', 'usher','Instagram-Worthy', 'trip', 
'Pickup', 'Day', 'Year',  'Flights', 'Advanced', 'Bikaner', 'Out', 'Entertainment', 'hot', 'relaxing', 'Jaipur', 'Monday', 
'errores', 'Station', 'Hide', 'Sign', 'Check', 'travel', ';', 'BEX', 'dream', 'list','Hiking', 'hotels', 'Us', 'lingers', 'majestic',
'Where', '22/08/2018', 'Inc.', 'planning', 'Exploring', 'pondicherry','Actions', 'points', 'If', 'Attractions', 'Activities', 'Food', 
'city', 'Rewards', 'IndiaInspirationStaycationsTips', 'thanks', 'The', 'Today','room', 'While', 'At', 'majesty', 'Naturally', 
'Licence', 'Follow', 'Archives', 'CulturalExperienceIndia', 'Tour', 'flights', 'Nagpur', 'Mehta', 'Hakeem', 'Beach', 'Aman', 'filled', 
'hide', 'Listopedia', 'Nikhil', '2019', 'temples', 'During', 'North', 'Hill', 'Qillas', 'Republic', 'Temples', 'delivery', 'karnataka', 
'route', 'Tasmai',  'fancy', 'living', 'A', 'Return', 'Comments', 'Show', 
'like', 'Find', '3', 'No', 'Saksena','Anam', 'get', 'awesome', 'Type', 'ways', 'Car', 'best', 'Bank', 'Airport', 'Lakes',
'チェックイン', 'past', 'street', 'Tamil', 'region', 'Eve', 'Summer', 'followers', 'festivals', 'nature', 'Read','town', 'sights', 
'Three', 'From', 'Deals', 'little', 'ol', 'week', 'Long', 'Madurai', 'expansive', 'occasion', 'land', 'Delhi', 'architecture',
'You', 'Posts', 'Triangle', '↑', 'Do', 'former', 'things', 'great', 'tourist', 'holiday', 'Nightlife','River', 'IndiaWeekend', 
'Additional', 'standing', 'So', 'Underrated', 'experiences', 'global', 'history',  'us', 'triangle','Honeymoon', 'Drink', 'sun',
'first', '05/09/2017', 'Festivals', 'Video', 'Celebrate', 'fantastic', 'Holdings', 'congested','Singapore', 'reality', 'acquainted',
'Theme', 'series', 'largest', 'days', 'balcony', 'Comment', 'Destinationstravel-guide','Class', 'Lanka', 'Jyotsna', 'Getaways', 
'Maharashtra', 'Feedback', 'Sri', '1', 'Options', 'occurs', 'Ghosh', 'siguientes', 'Smashing', 'Mughal', 'online', 'Gold', 
'Outdoors', 'destination', 'Yamuna', '’', 'easy', 'preferida', 'New', 'Habitaciones', 'steps', 'bucket','It', 'rajasthan',
'Uttar', 'Places', 'trips', 'Hot', 'decided','holidays', 'tourism', 'overlooking', 'attractions','journey', 'got', 'Onactivities', 
'About', 'work', 'plans', 'Mahals', 'Our', 'Time', 'sunny', 'ActivitiesFestivals', 'Stay', 'Inspiration','Europe', 'Authors', 
'Mountains', 'takes', 'Trip', 'celebrate', 'London', 'In', 'Delivery', 'Sandy', 'imagine', 'Holidays', 'Agra', 'company', 'Luxury', 
'buildings', 'Meghalaya', 'idea', 'climate', 'leading', 'banks', 'Breaks', 'way','IndiaTop', 'surely', 'due', 
'Ideas', 'kerala', 'Hotel', 'Museums', 'Interesting', 'presence', 'Mauritius', 'Itineraries', 'UNESCO', "P'Roza", 'joy', 'Parks',
'look', 'Vuelo', 'Active', 'Minute', 'reembolsable', 'Destination', 'Varanasi', 'major', 'urban', 'L�nea', 'York', 'signing',
'Golden','equipment', 'help','Weekend', 'Pradesh', 'Heritage', 'As', 'To', 'Back', 'Things', 'diaries', 'experience',  'requirement', 
'Gautam', 'Train', '14', 'district', 'bags', 'World', 'Kuala', 'About', 'soul', 'After', 'Sightseeing', 'better', 'Pilgrimage', 'hap', 
'East', 'nothing', 'Culture', 'region', 'Lakeside', 'feel', 'Mumbai', 'Triangle', 'trip', 'Future', 'Five', 'Delhi', 'Vrindavan', 
'Quaint', '1900+', 'Stop', 'Published:07', 'Home', 'Posts', 'Star', 'Reckoned', 'guide', 'No', 'Singh', 'ever', 'country','insightful',
'immortal', 'Kashmir', 'trekking', 'Jatin', 'run', 'Lake', 'Firecrackers', 'away', 'Easy', 'Horror', 'Parks', 'Peace', '7', 'Person',
'Works', 'Wildlife', 'Dham', 'Museums', 'Buddha', 'Shuva', 'Roopkund', 'Safety', 'Pineapple', 'Sitemap', 'year', 'air', 'Package', 
'Coffee', 'Jharkhand', 'Religious', 'Tourism', 'Elephant', 'Season', 'Gurung', 'buffs', 'Published:25', 'joy', 'This', 'feeds', 'trek', 
'Jan', 'Published:17', 'Fed', '+91-921', 'Contact', 'Tickets', 'Published:23', 'Travelling', 'Dec', 'ranges', 'Visit', 'What', 'Prices', 
'Maldives', 'Vacation', 'see', '7223/24', 'Mathura', 'wash', 'Indonesia', 'hours', 'evident', 'outside', 'Trip', 'self', 'PLAN', 
'Happiest', '©', 'valley', 'retreat', 'Lost', 'While', 'Stay', 'March', 'Kerala', '/', 'If', 'ideas', 'Wedding', 'holy', 'Table',
'uni', 'Uttarakhand', 'Darshan', 'Life', 'November', 'Book', 'dwell', 'ready', 'Cultural', 'Corbett', 'earthy', 'etched', 'Boat', 
'plan', 'Chamoli', 'Ranthambore', 'Indian', 'read', 'Us', 'season', 'package', 'Lesser-Known', 'Plan', 'Beach', 'something', 'smells',
'Mobile', 'Didn', 'Packages', 'Library', 'Join', 'Their',  'International', 'become', 'based', 'nature', 'And', 'Deb', 'Facebook', 
'BC', 'Top', 'Pallavi', 'insights', 'time', 'Heritage', 'Ensuring', 'TRIP', 'all-round','Van', 'offer', 'Abhishek', 'opens', 
'Festival', 'Found', 'June', 'Best', 'Kanchenjunga', 'Kapoor', 'Himalayan', 'Self', 'Published:01', 'ABOUT', 'Place', 'Own', 
'InternationalNEW', 'All', 'Mexico', 'Tamil', 'Published:20', 'winning', 'confluence', 'Hill', 'Station', 'Hotels', 'Gorgeous', 
'tips', 'Bengaluru', 'evergreen', 'Swati', 'Holiday', 'Tiger', 'Thapliyal', 'Things', '?', 'App', 'bring', 'Flight', 'Career', 'Social', 
'Pass', 'Temples', '*', 'tour', 'Chopta', 'Published:04', 'Fighting', 'Gulmarg', 'Holidays', '6', '2019', 'Oct', 'storm', 'Kolkata', 
'Let', 'Snow', 'Lavish', 'Facts', 'since', 'stunning', 'Nov', '19', 'Parvati', 'Experience', 'ground', 'destinations', 'enchanting', 
'Updated', 'Published:08',  'Pregnant', 'Tanisha', 'tourists', 'Reserve', 'For', 'clouds', 'An', 'Tigers', 'Temple','enigma', 'worthy', 
'Published:02', 'skiing', 'Tourist', 'Leopard', 'Brata', 'How', 'let', '+91-9212777225', 'Places', 'Tell', 'ID', 'South', 'Know', 
'Nepal', 'spiritual', 'Park', 'makes', 'Enjoying', 'Ashwini', 'Flowers', 'Jaisalmer', 'Twinkle',  'range', 'indelible', 'Trekking', 
'within', 'Spiritual', 'state', 'winter', 'Joshi', 'adventure', 'Where', 'TMI', 'Followers', 'Family', 'Nidhi', 'Published:03', 'July', 
'Tourmyindia.com', 'biosphere', 'league', 'Monsoon', 'Living', 'find', 'Roy', 'Himachal', 'enthrall', 'Sham', 'Ayurveda', 'details', 
'Linkedin', 'Trek', 'wildlife', '’', 'Grab', 'Seven', 'remains', 'Alerts', 'blossoms', 'Hindu', 'Offbeat', 'You', 'Painful', 'packing', 
'Dharamshala', 'Published:30', 'tourmyindiadelhi', 'Offer', 'Name', 'Bangkok', 'Travel', 'enligh', 'Adventure', 'Beauty', 'Health', 
'Bengal', 'trips', '4', 'Rajasthan', '20', 'days', 'Your', 'park', 'People', 'Golden', 'fascinating', 'detailed','intriguing', 
'Interest', 'Skype', 'pump', 'world', 'Glimpse', 'Nadu', 'Inspirational', 'charm', 'Our', 'Incredible', 'exciting','looking',
'shrines', 'Importance', 'Insight', 'Here', 'Published:14', '1', 'Stations', 'Tips', 'Amazing', 'The', 'freedom', 'NEW', 'entici', 
'Discover', 'Insights', 'Retreat', 'Published:24', 'daily', 'experts', 'like', 'Published:18', '140K+', 'Malaysia', 'Call', 'ultimately', 
'high-altitude', 'I', 'Beaches', 'celestials', 'national', 'Dzongri', 'featuring', '24', 'Soaring', '2018', '-', 'Which', 'Dies', 
'Punakha', 'Cheap', 'Markha', '2', 'Devi', 'India', 'Indus', 'Stuffed', 'heavenly', 'cradle', 'landscapes', 'Luxury', 'Story', 'yes',
'Tranquility', '8', '3500+', 'Email', 'Bhutan', '15', 'Tours', 'Mostly', '31', 'Mar', 'Nanda', '16', 'Karnataka', 'calmness', 'Domestic', 
'Backwaters', '2200+', 'May', 'North', 'dust', 'many', 'holiday', 'High-Altitude', 'Trending', 'inner', 'McCluskieganj', 'River', '10', 
'Honeymoon', 'Town', 'rain', 'vast', 'Jun', 'readers', 'Vijayendra', 'Whts', 'Range', 'summer', 'consider', 'praises', 'Request', 'Have',
'Treks', 'Industry', 'Zanskar', 'fun', 'ideal', 'Vietnam', 'Sharma', 'See', 'get', 'REVIEWS', '...', 'conquer', 'Impact', 'Duration', 'Jim', 
'go', 'doubles', 'Ethereal', 'Assam', 'Ladakh', '277', 'Death', 'Well', 'submit', 'best', 'Aug', 'Featured', 'places', 'Visitors', 'coveted', 
'Break', 'destination', 'National', 'Thailand', 'Teachings', 'Chandrashila', 'Destinations', 'Inspired', 'Valley', 'Indulging', 'travelling', 
'unique', 'sacred', 'Madhya', 'Hamir', 'Vows', 'Summer', 'Jul', 'Tulip', 'lose', 'Sri', 'rights', 'October', 'Europe', 'Search', 'right', 
'interesting', 'peace', 'start', 'Feb', 'Arun', 'Road', 'Dalhousie', 'back', 'Sundarbun', 'Akshaya', 'lovers', 'Mishra', 'Wild', 'Videos', 
'visit', 'Goecha', '2021/', '!', 'dark', 'Romantic', '29', 'Making', 'Frozen', 'Chandigarh', 'romanticized', 'divinity', 'Published:19', 
'January', 'Vishwajit', 'useful', 'CLIENT', 'Mechuka', 'Published:27', 'My', 'Yourself', 'Days', 'Airlines', '2020', 'During', 'Embody', 
'Anything', 'form', 'T-104', 'Twitter', 'pilgrimage', 'Hooghly', 'Weekend', 'different', 'place', '×', 'Dirt', 'Nights', 'Enjoy', 'Deals', 
'formed', 'Apr', 'Offering', 'Goa', 'natural', 'Edu-Tourism', 'Pin', '–', 'customised', 'heart', 'Published:21', 'Lumpur', 'deal', 'High', 
'Most', 'Published:16', 'wond', 'Died', 'safari', '2021', 'Some', 'Read', 'Who', 'reserved', 'Listen', 'Activities', 'Dubai', 'US', 
'grumble', 'inspiration', 'More', 'enjoy', 'Exciting', 'Latest', 'YOUR', 'Famous', 'Blog', 'April', 'tropical', 'abroad', 'importan', 
'Between', 'mystical', 'Australia', 'Full', 'travel', 'Pra', 'unblinking', 'Dehradun', 'Kedarnath', 'Himalayas','Magical', 'Cruise', 
'Looking', 'Instagram', 'wilderness','Share', 'Need', 'Ultimate', '18', '12', 'petrichor.', 'Tour', 'Country', 'Descriptions', 
'Arunachal', 'collection', 'LET', 'Bangalore', 'Mexican', 'Published:26', 'Popular', 'Quote', 'Dates', 'breathtaking', 'Do', 'long', 
'Yes', 'Books', 'Sikkim', 'reserve', 'around', 'City', 'Recommended', 'Anand', 'duri', 'Lanka', 'treks', 'Nagaland', 'Perfect', 'Tritiya', 
'Sanctuaries', 'blend', 'art', 'UAE','Getaways', 'Pradesh', 'pulsating', 'Singapore', 'Reasons', 'Demons','let', 'exchanging','portals', 
'learn', 'exciting', 'Close', 'there.The',  'Devi', 'MANGALA', 'stations', 'The', 'memorable', 'Be', 'benefits', 'Venture', 'awesome',
'FORESTIn', 'IN', 'Use', 'TEMPLE', 'easily', 'visiting', 'websites', 'recently', 'Tours', '100', 'Travel', 'Read', 'takes', 'If', 
'travelers', 'World', 'Blog', 'looking', 'us', 'places', 'BlogsA', 'backwater', 'together', 'hands', 'Mount-', 'deciding', 'better', 
'tales', 'avail', 'free', 'Flight', 'biggest', 'holidays', 'packages', 'Memorable', 'world', 'contact', 'Marketing', 'Airport.List', 
'quality', 'fort', 'area', 'Observe', 'Popular', 'marine', 'calms', 'part', '...', 'water', 'deals', 'nature','Road', 'Indian', 'melam',
'country', 'Day', 'host', 'receive', 'stay', 'Check', 'kerala.Top', '&', 'India.Novotel', 'reputed', 'district', 'areas', 'ibis', 
'booking', 'every', 'WaterfallsIn', 'Billion', 'dedicated', 'like', 'list', 'touch', 'welcome', 'view', 'Palai', 'Forum', 
'DestinationsTravel', 'homestays', 'Books', 'Miles', 'Holidays', 'contributors', 'Ernakulam', 'Kerala.Accommodation', 'work', 
'magnificent', 'magical', 'Digital', '–', 'Authentic', 'Guide', 'Kochi', 'THE', 'vibrant', 'travelogues', 'thrilling', 'holy', 
'proposal', 'Online', 'including', 'flyer', 'There', 'Chenda', 'really', '©', '|', '!', 'Queries', 'Indo', 'posts', 'festival', 
'KANNAGI', 'enjoyed', 'true', 'experience', 'valiant', 'etc', 'sieges', 'Share', 'A', 'operators', 'Fort',  'LoginRegister', 
'program', 'BlogsDestinations', 'population', 'Bhadrakali', 'Festival', 'Kannagi', 'explore', 'various', 'It', 'tourist', 'Travelholic', 
'Travelouge', 'I', 'recent', 'explain', 'review', 'reward', 'year', 'Idukki', 'offer', 'underwater', 'travellers', 'join', 'houseboats', 
'business-friendly', '2020', 'latest', 'About', 'Preparation', 'first-hand', '5-star', 'based', 'exchange', 'Follow', 'INSIDE', 'Thinking', 
'adventure', 'share',  'real', 'introduce', 'Nadu', 'ideal', 'accommodation', 'experience.Scuba', 'Temple', 'month', 'Elephant', 
'amenities', 'smaller', 'remote', 'ways', 'earn', 'content', 'Do', 'Waterfalls', 'Homestays', 'flight', 'Tips', 'destination', 'exploring', 
'resorts', 'India', 'Airways', 'TipsTravel', 'vacation', 'Abroad', 'Hotel', 'scuba', 'relax', 'itinerary', 'blogs', 'must', 'parts', 
'We', 'Being', 'Jauhar.The', 'Kovalam', 'goddess', 'stories', 'considered', 'Kodaikanal', 'river.St', 'Us', 'promotion', 'feel', 
'questions', 'cruises', 'people', 'lodges', 'travel', 'Jet', 'AdSense', 'information', 'trip', 'visited', '%', 'forest', 'border', 
'place', 'Plan', 'tour', 'events', 'KeralaAre', 'personally', 'accessible', 'backwaters', 'An', 'Join', 'frequent', 'calling', 
'IndiaTravelBlog.com', 'misty', 'focus', 'Articles', 'Valparai', 'One', 'Tamil', 'Cochin', 'joyful.Popular', 'Rajasthan', 'blogger', 
'Kerala', 'Infopark', 'providing', 'Book', 'history', 'pilgrim', 'Safari', 'DEVI', 'hill', 'Kurumpanmoozhy', 'hotels', 'historical', 
'cultural', 'effigy', 'incarnation', 'Then', 'articles', 'Ideas', 'holiday', 'collaborate', 'food', 'Experience', '-', 'SpiderWorks', 
'Are', 'blog', 'partner', 'Privacy', 'program.More', 'diving', 'mutual', 'Machattu', 'readers', 'This', 'beaches', 'Sabarimala', 'guest', 
'unexplored', 'Life', 'Policy', 'IDUKKI', 'enjoy', 'go', 'romance', 'Panamkudantha', 'UnknownIn', 'Hotels', 'concerns', 'published', 
'Planning', 'close', 'Ernalukam', 'battles', 'believe', 'Let', 'accept', 'visit', 'Technologies', 'day', 'temple', 'Novotel', 
'Chittorgarh', 'organized', 'DestinationsKeralaGoaAndaman', 'Here', "'s", 'Blogs', 'destinations', 'pamba', 'several', 'Diving', 
'link', 'IslandsForumSubmit', 'kings', 'Business', 'Mangala', 'Nicobar', 'February', 'amazing', 'top', 'lakes', 'Village', 'PostsThe', 
'Terms', 'make', 'provide', 'villages', 'know', 'using', 'Destinations', 'beside', 'RESERVES', 'Mamangam', 'foodie', 'Horse', 'life', 
'All', 'Contact', 'online', 'premium', 'splendid', 'Packages', 'TIGER', 'regarding', 'Featured', 'MG', 'Bond', 'Try', 'top-notch', 
'PERIYAR', 'include', 'best', 'stay.More', 'relaxing', 'going', 'You', 'around', 'South', 'Copyright', 'interested', 'experienced', 
'find', 'mountains', 'LOCATED', 'Thomas', 'write', 'mind.Come', 'lowest', 'happen', 'restaurants', 'Tour', 'details', 'famous', 
'available', 'revenue', 'business', 'ExperienceInternationalIndian', 'flabbergasted', 'architecture', 'bloggers', 'go.Review', 
'article', 'Knowing', 'located', 'much', 'hilltop', 'prices', 'walk', 'shared', 'Udaipur'])




def allfunctioncall(url):
  # we are checking the excel file and image if they are exist then we delete and new excel and image store over there
  if os.path.exists("F:\\ProjectDjango\\websiteanalyzer\\static\\matchingpercentage.png"):
    os.remove("F:\\ProjectDjango\\websiteanalyzer\\static\\matchingpercentage.png")
  if os.path.exists("F:\\ProjectDjango\\websiteanalyzer\\templates\\Excel\\Matchingpercentage.xlsx"):
    os.remove("F:\\ProjectDjango\\websiteanalyzer\\templates\\Excel\\Matchingpercentage.xlsx")

  # store all data set in a dictonary 
  alldataset = {"DharmikSite":dharmiksite, "SchoolorCollege":schoolorcollage, "ProgrammingTutorial":programmingtutorial, "TravellingBlog" : travellingblog}
  
  # call getUrlContent, cleaname and contentProcessing function for scrap, clean and convert in wordset and key value pair.
  htmlpage = getUrlContent(url)
  content = cleanme(htmlpage)
  wordset, keyvaluepairs = contentProcessing(content)

  # inisilize some variable for storing data
  valueset = set()
  matchinpercentagedict = {}
  allresultlist = []
  keyvaluepairdict = {}
  detaillist = []
  

  for i in alldataset:

    # resultlist list and newset dictornary inslize for storing data with every dataset 
    resultlist = []
    newset = {}
    #print("keyname = ", i)
    valueset = alldataset.get(i)
    #print(len(valueset))
    #print(valueset)
    resultlist = resultlist + ["Category : {0}".format(i)]
    matches = valueset.intersection(wordset)
    #print(matches)
    lenofmatches = len(matches)
    lenofkeyvaluepair = len(valueset)
    #print("No of element matches to set =",lenofmatches)
    resultlist = resultlist + ["No of Matches = {0}".format(lenofmatches)]
    matchinpercentage = (lenofmatches/lenofkeyvaluepair)*100
    

    # round use for get value from decimal 2 digit and store all the data with key and values in matchingpercentage dictonary
    matchinpercentage = round(matchinpercentage,2)
    matchinpercentagedict[i] = matchinpercentage


    # append lenofmatches and lenofkeyvalurpair and maching percentage in detaillist
    detaillist.append(lenofkeyvaluepair)
    detaillist.append(lenofmatches)
    detaillist.append(matchinpercentage)
    
    

    
    # store all match word  frequency in keyvaluepair dictonary 
    for x in keyvaluepairs:
      if x[0] in matches:
        newset[x[0]]=x[1]
      keyvaluepairdict[i] = newset


# Write word frequency in excel
  for key1 , val1 in keyvaluepairdict.items():
    #print(key1)
    key = val1.keys()
    val = val1.values()
    tempdict = {"Words":list(key),"Frequency":val}
    df1 = pd.DataFrame(tempdict)
    #print(df1)
    df1.to_excel("F://ProjectDjango//websiteanalyzer//templates//Excel//{0}.xlsx".format(key1),index=False)
  

  #print(matchinpercentagedict)
  #print(allresultlist)
  #print(wordset)

  # store the matchingpercentagedict in a dataframe because of removing garbej value
  df = pd.DataFrame(list(matchinpercentagedict.items()),columns=['Dataset','Percentage'])
  df.to_excel("F://ProjectDjango//websiteanalyzer//templates//Excel//Matchingpercentage.xlsx",index=False)

  data = pd.read_excel("F:\\ProjectDjango\\websiteanalyzer\\templates\\Excel\\Matchingpercentage.xlsx")
  #print(data)


  #figname = random.randint(111,111111)
  figname = "Matchingpercentage"
  plt.rcParams['figure.figsize'] = [10, 5]
  #plt.rcParams.update({'font.size':7})
  data.plot(kind='bar',x='Dataset',y='Percentage',width=0.20)
  plt.xticks(rotation=0, horizontalalignment="center")
  plt.xlabel("Category",fontweight='bold',fontsize=10)
  plt.ylabel("Matching Percentange ",fontweight='bold',fontsize=10)
  plt.title(url,fontsize=10,fontweight='bold')
  plt.savefig("F://ProjectDjango//websiteanalyzer//static//{0}".format(figname))
  #plt.show()
  
  
  return matchinpercentagedict,figname, detaillist


#alldataset = {"DharmikSite":dharmiksite, "School/College":schoolorcollege, "ProgrammingTutorial":programmingtutorial, "TravellingBlog" : travellingblog}
#print(keyvaluepairs)

"""
currenturl = "http://varanasikshetra.com/"
matchpercentage,figname,detaillist =  allfunctioncall(currenturl)



print(matchpercentage)
print(allresultlist)
print(figname)
"""