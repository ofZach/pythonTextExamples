#!/usr/bin/python
# coding: utf-8
#
# World Clock, copyright (c) 2013 Nick Montfort <nickm@nickm.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# 27 November 2013

from datetime import datetime
from random import choice, shuffle, random
import pytz

def frontmatter():
    print '\pagenumbering{gobble}'
    print
    print '## World Clock'
    print '\pagebreak'
    print
    print '&nbsp;'
    print
    print '\pagebreak'
    print
    print '# World Clock'
    print
    print '## Nick Montfort'
    print
    print 'Bad Quarto'
    print 'Cambridge,'
    print 'Massachusetts'
    print
    print '\pagebreak'
    print
    print 'Copyright &copy; 2013 Nick Montfort'
    print
    print 'Generated (with free software) &amp; printed in the United States of America'
    print '\pagebreak'
    print
    print '>The originality of _One Human Minute_ lies in its being not a statistical compilation of information about what has taken place, like an ordinary almanac, but rather _synchronous_ with the human world, like a computer of the type that we say works in real time, a device tracking phenomena as they occur.'
    print '>'
    print '>&mdash;Stanislaw Lem'
    print
    print '\pagebreak'
    print
    print '&nbsp;'
    print
    print '\pagebreak'
    print '\pagenumbering{arabic}'

def fresh(x):
    i = int(len(x)/2 + random() * (len(x) - len(x)/2))
    return [x[i]] + x[:i] + x[i+1:]

now = ['only a moment before', 'almost', 'right about', 'exactly', 'precisely', 'right at', 'as it happens']

negative = ['furtive', 'ramshackle', 'decrepit', 'cookie-cutter', 'undistinguished', 'typical', 'run-down', 'small', 'dim', 'plain', 'ordinary', 'cramped']
shuffle(negative)

positive = ['sturdy', 'charming', 'tidy', 'homey', 'suitable', 'adequate', 'sound', 'orderly', 'nestlike', 'comfortable', 'nice', 'decent']
shuffle(positive)

place = ['habitat', 'accommodation', 'shelter', 'residence', 'domicile', 'abode', 'habitation', 'dwelling', 'structure', 'location', 'house', 'edifice']
shuffle(place)

a_man = ['an individual', 'someone', 'a man', 'a person', 'a youth', 'an old man']

a_woman = ['an individual', 'someone', 'a woman', 'a person', 'a youth', 'an old woman']

named = ['named', 'named', 'named', 'named', 'known as', 'who is called']

male_names = ['Abdallah', 'Abdel-Rahman', 'Abi', 'Abinet', 'Abraham', 'Ahmed', 'Ali', 'Amanual', 'Araya', 'Asfaw', 'Bereket', 'Berhane', 'Bilal', 'Biniam', 'Biruk', 'Daniel', 'Dawit', 'Derege', 'Elias', 'Ephrem', 'Ermias', 'Eyobel', 'Ezra', 'Fasil', 'Gebre', 'Haile', 'Halim', 'Hamza', 'Hanok', 'Hassan', 'Hewan', 'Hussein', 'Ibrahim', 'Karim', 'Khaled', 'Kidus', 'Kirubel', 'Mahmoud', 'Mathios', 'Melak', 'Mohammed', 'Murad', 'Mustafa', 'Nahum', 'Omar', 'Robel', 'Selim', 'Shewit', 'Tadesse', 'Taha', 'Tamiru', 'Tamrat', 'Tareq', 'Teodros', 'Yared', 'Yassin', 'Yonas', 'Yordanos', 'Youssef', 'Zecharias', 'An', 'Bo', 'Cheng', 'De', 'Dong', 'Feng', 'Gang', 'Guo', 'Hui', 'Jian', 'Jie', 'Kang', 'Liang', 'Ning', 'Peng', 'Tao', 'Wei', 'Yong', 'Wen', 'Alexander', 'Sergei', 'Dmitry', 'Andrei', 'Alexey', 'Maxim', 'Evgeny', 'Ivan', 'Mikhail', 'Artyom', 'Bill', 'Jim', 'Nick', 'Darius', 'Leonardo', 'Scott', 'Christian', 'Darren', 'Kenny', 'Brad', 'Zenon']
shuffle(male_names)

female_names = ['Abeba', 'Alem', 'Almaz', 'Ashraqat', 'Aya', 'Azeb', 'Bethlehem', 'Dalal', 'Desta', 'Doha', 'Eden', 'Elsa', 'Fajr', 'Farida', 'Fatima', 'Fatin', 'Fatma', 'Feven', 'Gamalat', 'Gamila', 'Haben', 'Habiba', 'Hasnaa', 'Helen', 'Hosna', 'Hosniya', 'Jerusalem', 'Kedist', 'Leah', 'Lili', 'Luwam', 'Lydia', 'Maha', 'Mahlet', 'Manna', 'Marone', 'Messeret', 'Rahiel', 'Reem', 'Rowan', 'Ruth', 'Saba', 'Sahar', 'Samrawit', 'Sara', 'Senait', 'Shahd', 'Shaimaa', 'Shewit', 'Suha', 'Tigist', 'Tizita', 'Tsega', 'Tsege', 'Yeshi', 'Yohana', 'Zewdy', 'Ai', 'Bi', 'Cai', 'Dan', 'Fang', 'Hong', 'Hui', 'Juan', 'Lan', 'Li', 'Lian', 'Na', 'Ni', 'Qian', 'Qiong', 'Shan', 'Shu', 'Ting', 'Xia', 'Xian', 'Yan', 'Yun', 'Zhen', 'Anastasia', 'Yelena', 'Olga', 'Natalia', 'Yekaterina', 'Anna', 'Tatiana', 'Maria', 'Irina', 'Yulia', 'Jennifer', 'Katie', 'Ali', 'Buffy', 'Christie', 'Stephanie', 'Vanessa', 'Johanna', 'Amaranth', 'Jill', 'Katarzyna']
shuffle(female_names)

size = ['is on the small side', 'is of completely average stature', 'is rather large', 'towers over most people', 'usually turns to look up to other people', 'is significantly smaller than others of the same age', 'is quite sizable and imposing', 'is no larger or smaller than one would expect']
shuffle(size)

packaging = ['the ingredient list', 'the warning message', 'some sort of exclamation', 'an entirely made-up word', 'a tiny numeric code']

product = ['on a box of breakfast cereal', 'on an over-the-counter drug container', 'on a small packet', 'off the label of a tin can', 'from a recipe clipping']

condition = ['crumbling', 'well-preserved', 'pristine', 'wrinkled', 'stained', 'canary-colored', 'embossed']

document = ['letter', 'certificate', 'note', 'manuscript', 'contract', 'report', 'envelope', 'card']

action = ['nods, very deliberately', 'raises one eyebrow', 'looks away, then back', 'chews a fingernail', 'sits up straight', 'suddenly collapses', 'scratches one ear', 'zones completely out', 'hums quietly', 'turns entirely around', 'smiles a tiny smile', 'frowns a slight frown']

#frontmatter()

for hour in range(24):
    #print
    #print '## ' + str(hour)
    #print
    for minute in range(60):
        now = fresh(now)
        negative = fresh(negative)
        positive = fresh(positive)
        modifiers = [negative[0], positive[0], positive[0] + ' yet ' + negative[0], negative[0] + ' yet ' + positive[0]]

        place_adj = choice(modifiers)

        print place_adj

        pronoun = choice(['He', 'She'])
        if pronoun == 'He':
            male_names = fresh(male_names)
            name = male_names[0]
            a_man = fresh(a_man)
            person = a_man[0]
        else:
            female_names = fresh(female_names)
            name = female_names[0]
            a_woman = fresh(a_woman)
            person = a_woman[0]

        named = fresh(named)
        size = fresh(size)
        if choice(['product', 'document']) == 'product':
            packaging = fresh(packaging)
            product = fresh(product)
            reading_matter = packaging[0] + ' ' + product[1]
        else:
            condition = fresh(condition)
            document = fresh(document)
            reading_matter = 'a ' + condition[0] + ' ' + document[0]

        action = fresh(action)

        utc_time = datetime(2000, 1, 1, hour, minute, 0, tzinfo=pytz.utc)
        tz_names = pytz.common_timezones[:-8]
        tz_names.remove('GMT')
        tz_names.remove('Antarctica/South_Pole')
        tz_names.remove('Antarctica/DumontDUrville')
        tz_names.remove('Canada/Atlantic')
        tz_names.remove('Canada/Central')
        tz_names.remove('Canada/Eastern')
        tz_names.remove('Canada/Mountain')
        tz_names.remove('Canada/Newfoundland')
        tz_names.remove('Canada/Pacific')
        tz_names.remove('Pacific/Easter')
        tz_name = choice(tz_names)
        new_zone = pytz.timezone(tz_name)
        loc_time = utc_time.astimezone(new_zone)
        current_local_time = loc_time.strftime('%H:%M')
        locale = tz_name.split('/')[-1]
        locale = ' '.join(locale.split('_'))
        if locale in ['Maldives', 'Azores', 'Isle of Man', 'Vatican']:
            locale = 'the ' + locale
        if locale in ['Canary', 'Faroe']:
            locale = 'the ' + locale + ' Islands'
        if locale[:3] == 'St ':
            locale = 'St. ' + locale[3:]

        #print 'It is now ' + now[0] + ' ' + current_local_time + ' in ' + locale + '. In some ' + place_adj + ' ' + choice(place) + ' ' + person + ' ' + named[0] + ' ' + name + ', who ' + size[0] + ', reads ' + reading_matter + '. ' + pronoun + ' ' + action[0] + '.'
        #print
    #print '\pagebreak'
