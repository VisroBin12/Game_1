from random import randint
from time import sleep

prise_1=25
prise_4=40
upgrade_attack=0.5
upgrade_armore=0.05
prise_5=1
prise_2=1
prise=prise_1*prise_2
prise_3=prise_4*prise_5
prise_6=1
prise_7=1
prise_8=1
sell_luck=1

inventory_name_1='Обрывки фолиантов в желе'
inventory_name_2='Золотой клык'
inventory_name_3='Сердце голема'
inventory_name_4='Порванный саван Бога Смерти Яропанага'
inventory_name_5='Корона Смерти'

player = {
    'title': 'Путешественник',
    'name': '',
    'armor': 0.95,
    'armor_dop': 1,
    'hp': 100,
    'attack': 4.5,
    'luck': 4,
    'money': 100,
    'inventory': []
}

enemies = [
    {
        'name': 'Слизь',
        'hp': 15,
        'attack': 7.5,
        'armor' : 1,
        'place':'Ты видищь обычную, лесную поляну на которой кто-то рассыпал мешок древних фолиантов, которые сейчас уже доедает средних размеров синий комок слизи',
        'script': 'Блёб-блёп. *Ты видиш как слизь вибрирует словно желе при твоём приближении*',
        'enemy_inventory': ['Обрывки фолиантов в желе'],
        'random':3,
        'gold': randint(1,12),
        'win': '*Слизень сдувается и оставляет после себя лишь лужу слизи с обрывками фолиантов*.',
        'loss': 'Блёп-Блёб. *Слизь медленно уползает доедать фолианты*'
    },
    {
        'name': 'Ликантроп',
        'hp': 25,
        'attack': 16,
        'armor' : 0.70,
        'place':'Зайдя глубоко в лес, ты наткнулся на старый, лесничий домик, но что-то в нём странно. Перед тобой стоит выбор: Зайти в дом и осмотреть его изнутри или уйти... а нет, выбор уже сделали за тебя. Перед тобой Ликантроп',
        'script': 'Беги отсюда человек, пока я ещё могу себя контролировать, а иначе ты станешь моим ужином!',
        'enemy_inventory': ['Золотой клык'],
        'random':5,
        'gold': randint(215,487),
        'win': 'Наконец....Вальхалла. *Ты видишь как Ликантроп испустил последний дух с облегчением и счастьем на своей морде*',
        'loss': 'А мог ведь жить, если бы меня послушал, зато теперь будет что поесть перед работой.'
    },
    {
        'name': 'Каменный  голем',
        'hp': 80,
        'attack': 26,
        'armor' : 0.57,
        'place':'Недалеко от Крипты ты видишь огромного Коменного голема, который будто патрулирует вход в Крипту',
        'script': 'Каменный голем скрипит камнями, двигаясь в твою сторону',
        'enemy_inventory': ['Сердце голема'],
        'random':6,
        'gold': randint(763,1264),
        'win': '*Рассыпаясь, голем будто успевает показать тебе один из пальцев на правой руке*.',
        'loss': '*Голем отворачивается от твоего тела и уходит на дальнейшее патрулирование*'
    },
    {
        'name': 'Проекция Бога Смерти Яропанаг',
        'hp': 143,
        'attack': 33,
        'armor' : 0.43,
        'place':'Зайдя в Крипту, ты видишь мрачные коридоры с огромным количеством гробов, находящихся в стенных нишах. Пробираясь сквозь огромные и когда-то величественные залы, ты вдруг слышишь громоподобные слов',
        'script': 'Ты всё таки добрался *Слова ты слышишь прямо у себя в голове, и каждое из них заставляет тебя дрожать от страха пред древностью и мощью произнёсшего из*',
        'enemy_inventory': ['Порванный саван Бога Смерти Яропанага'],
        'random':7,
        'gold': randint(1500,2257),
        'win': 'Ты ещё не достаточно сделал *После этих слов загорается огромный ритуальный круг и тело Проекции Бога Смерти Яролпанага рассыпается прахом.*',
        'loss': 'Ты слаб, но хоть послужишь дополнением к моей коллекции. *Перед затуханием сознания ты видишь, как твоё тело медленно становится Рыцарем Смерти* '
    },
    {
        'name': 'Бог Смерти Яропанаг',
        'hp': 200,
        'attack': 47,
        'armor' : 0.33,
        'place':'Пройдя в самые глубины Крипты, ты видишь огромный и всё ещё величественный, пусть и потускневший от времени зал, в котором рядами вдоль стен стоят доспехи столь искусной работы, что позавидовали бы и короли. И вновь ты слышишь громоподобный голос',
        'script': 'Ну что-же... Ты добрался до самых глубин моей тюрьмы... Прими же обьятия Смерти. *После этих слов вокруг всё задрожало, а перед тобой проявился параллельный мир, в котором находилось основное тело Яралпанага* ',
        'enemy_inventory': ['Корона Смерти'],
        'random':1,
        'gold': randint(3000,4000),
        'win': '*Тело Яролпанага разрушается и ты видишь, как параллельный мир умирает вместе с богом. Ты чудом успеваешь выбежать из крипты, прихватив с собой Корону и мешочек с золотом*',
        'loss': '*Твоё тело рассыпается под действие ужасающих заклинаний Бога Смерти* -К сожалению ты не увидишь следующий рассвет жизни.'
    }
]
player_inventory=player['inventory']
name = input('Введи своё имя, путник: ')
player['name'] = name


def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    enemy_armor = enemies[current_enemy]['armor']
    print(f'Событие - {enemy["place"]}')
    sleep(1)
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    stat=int(input('Желаешь посмотреть характеристики врага? (да(1)/нет(2))'))
    if stat==1:
        print(f'Имя противника: {enemy["name"]}')
        print(f'Здоровье противника: {enemy["hp"]}')
        print(f'Атака противника: {enemy["attack"]}')
        print(f'Броня противника: {enemy["armor"]}')
        sleep(3)
        print()
    if stat==2:
        print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["title"]} {player["name"]} атакует {enemy["name"]}.')
            crit=randint(1,10)
            if crit < player['luck']:
                print('Критический удар!')
                enemy_hp -= player['attack']*2*enemy_armor
            else:
                enemy_hp -= player['attack']*enemy_armor
            sleep(1)
            print(f'''{player["title"]} {player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["title"]} {player["name"]}.')
            player['hp'] -= enemy['attack']*player['armor']*player['armor_dop']
            sleep(1)
            print(f'''{player["title"]} {player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        change=randint(1,10)
        if change>=enemy['random']:
            print(f'ты получаешь {enemy["enemy_inventory"]}')
            player['inventory']+=enemy['enemy_inventory']
        print(f'ты получаешь {enemy["gold"]} монет')
        player['money']+=enemy['gold']
        print(player['inventory'])
        print(player['money'])
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')

print(f'{player["title"]} {player["name"]}, Ты часто видел один и тот же сон, он приходил к тебе всегда неожиданно.')
sleep(2)
print('Этот сон всегда повторялся точь-точь и был слишком красочным и ярким, чтобы забыться с утренним пробуждением.')
sleep(2)
print('В этом сне ты видел огромное существо, что пожирало этот мир. Оно постоянно измняло свой облик и будто находилось где-то не здесь, а в другой реальности, а сюда попадала лишь небольшая крупица этого существа')
sleep(4)
print('Ты никогда не понимал что это за существо и почему оно тебе сниться. Ты пытался бороться с этими снами, обращался к алхимикам, но всё было бесполезно.')
sleep(3)
print('И вот, в одну из ночей этот сон неуловимо изменился. И ты вдруг понял, что видишь, что неподалёку от города Кранштейн открылись древние катакомбы, и тебя зовёт в них.')
sleep(4)
print('Не в силах сопротивляться зову, ты собрал свои пожитки, которые составили: пару сотен монет, кинжал, да старую и потёртую кожаную куртку, и отправился туда, куда тебя вёл зов.')
sleep(4)
print('Идти пришлось долго, а потому большую часть денег ты потратил и оставил лишь небольшой капитал, благодаря которому ты надеешься разобраться в своих снах')

while True:
    if player['money']>=12000:
        player['title']='Богач'
    if inventory_name_5 in player['inventory']:
        print('После сложного и долгого приключения, ты наконец получил уничтожил того, кто навевал на тебя эти сны, получил Корону Смерти самого Яропанага и наконец можешь спать спокойно.')
        sleep(4)
        print('О твоих делах ещё очень долго будут слагать легенды, как великие в своей чести, так и ужасные в своей жестокости.')
        sleep(3)
        print('Но для тебя это уже не важно, ведь ты навсегда покидаешь этот город и уходишь в закат.')
        sleep(2)
        print('23 июгуста 512 год до эры Бригонтов')
        break
    else:
        player['hp']=100*prise_6
        print('Ты стоишь у фонтана на главной площади маленького городка, под названием Кранштейн')
        sleep(2)
        print(f'{player["title"]} {player["name"]}, у тебя несколько вариантов. Пойти в торговый квартал (1), сходить в леса для охоты (2), глянуть инвентарь(3) или узнать свои характеристики(4)?')
        sleep(2.5)
        action= int(input('Что ты выбираешь?:'))
        if action==1:
            print('Ты пришёл в торговый квартал и у тебя несколько вариантов: Пойти к кузнецам(1), пойти к торговцам для продажи своих трофеев(2), пойти к алхимикам(3) или к закленателю(4)?')
            sleep(2)
            action_5= int(input('Куда пойдешь?'))
            if action_5==1:
                print('Ты пришёл к кузнецам, которые могу улучшить либо твоё оружие(1), либо твою броню(2).')
                action_1=int(input('Что ты выберешь?:'))
                if action_1 ==1:
                    if player['attack'] >=15:
                        print('Кузнец посмотрел на твоё оружие и сказал, что не может улучшить и без того превосходное оружие.')
                        print('Тебе ничего не остаётся, кроме как вернуться к фонтану.')
                        sleep(3)
                    else:
                        print(f'Кузнец посмотрел на твоё жалкое оружие и сказал: Я могу улучшить это за {prise_1}*{prise_2} монет')
                        action_2=int(input('Желаешь? (да(1)/нет(2)):'))
                        if action_2==1:
                            if player['money']>=prise_1*prise_2:
                                player['money']-=prise_1*prise_2
                                prise_2+=1
                                player['attack']+=upgrade_attack
                                print(f'У тебя в кошельке осталось {player["money"]} монет')
                                print(f'Твой урон теперь равен:{player["attack"]}')
                                print('После обновления оружия, ты возвращаешься обратно к фонтану')
                                sleep(3)
                            else:
                                print('Кузнец брезгливо морщится и отворачивается от тебя, бурча под нос что-то о нищих и работе за даром')
                                sleep(3)
                        else:
                            print('Кузнец равнодушно пожимает плечами и отворачивается от тебя')
                            print('Ты возращаешься обратно к фонтану и думаешь что делать дальше')
                            sleep(3)
                else:
                    if player['armor'] <= 0.5:
                        print('Кузнец посмотрел на твоё снаряжение и сказал, что не может улучшить и без того превосходное снаряжение.')
                        print('Тебе ничего не остаётся, кроме как вернуться к фонтану.')
                        sleep(3)
                    else:
                        print(f'Кузнец посмотрел на твоё жалкое снаряжение и сказал: Я могу улучшить это за {prise_4}*{prise_5} монет')
                        action_3=int(input('Желаешь? (да(1)/нет(2)):'))
                        if action_3==1:
                            if player['money']>=prise_4*prise_5:
                                player['money']-=prise_4*prise_5
                                prise_5+=1
                                player['armor']-=upgrade_armore
                                print(f'У тебя в кошельке осталось {player["money"]} монет')
                                print(f'Твоя защита теперь равна:{player["armor"]}')
                                print('После обновления снаряжения, ты возвращаешься обратно к фонтану')
                                sleep(3)
                            else:
                                print('Кузнец брезгливо морщится и отворачивается от тебя, бурча под нос что-то о нищих и работе за даром')
                                sleep(3)
                        else:
                            print('Кузнец равнодушно пожимает плечами и отворачивается от тебя')
                            print('Ты возращаешься обратно к фонтану и думаешь что делать дальше')
                            sleep(3)
            if action_5 ==2:
                print('Ты подходишь к торговцам всякой всячиной и самые разнообразные звуки бьют тебе по ушам. ')
                sleep(0.5)
                print('У самой большой лавки ты доску с написаными ценами на вещи, которые в этой лавке покупаются:')
                sleep(0.5)
                print('Обрывки фолинтов в желе: 45 монет')
                sleep(0.5)
                print('Золотой клык: 500 монет')
                sleep(0.5)
                print('Середце голема: 1300 монет')
                sleep(0.5)
                print('Любые вещи, напрямую связанные с богом смерти: 2500 монет')
                sleep(0.5)
                print('Из всех надписей тебя заинтересовали только эти')
                sleep(0.5)
                print('Желаешь ли ты, что-нибудь продать? (Ты продаёшь все предметы выбранного вида)')
                sleep(0.5)
                print(player['inventory'])
                action_6=int(input('(да(1)/нет(2)):'))
                if action_6==1:
                    print('Ты решаешь немного распродаться, но что ты хочешь продать?')
                    sleep(1)
                    action_7= int(input('Обрывки фолиантов в желе(1)/Золотой клык(2)/Сердце голема(3)/Вещь, связанная с богом смерти(4):'))
                    if action_7==1:
                        if inventory_name_1 in player['inventory']:
                            number_of_sale=player['inventory'].count('Обрывки фолиантов в желе')
                            for i in range(number_of_sale):
                                player['inventory'].remove('Обрывки фолиантов в желе')
                                player['money']+=45
                            print(f'Торговец забирает у тебя {number_of_sale} Обрывки фолиантов в желе и даёт тебе за него 45*{number_of_sale} монет')
                        else:
                            print('У тебя нет этого предмета, а потому ты, извинившись перед немного рассерженным торговцем уходишь обратно к фонтану.')
                    if action_7==2:
                        if inventory_name_2 in player['inventory']:
                            number_of_sale_2=player['inventory'].count('Золотой клык')
                            for i in range(number_of_sale_2):
                                player['inventory'].remove('Золотой клык')
                                player['money']+=500
                            print(f'Торговец забирает у тебя {number_of_sale_2} Золотой клык и даёт тебе за него 500*{number_of_sale_2} монет')
                        else:
                            print('У тебя нет этого предмета, а потому ты, извинившись перед немного рассерженным торговцем уходишь обратно к фонтану.')
                    if action_7==3:
                        if inventory_name_3 in player['inventory']:
                            number_of_sale_3=player['inventory'].count('Сердце голема')
                            for i in range(number_of_sale_3):
                                player['inventory'].remove('Сердце голема')
                                player['money']+=1300
                            print(f'Торговец забирает у тебя {number_of_sale_3} Сердце голема и даёт тебе за него 1300*{number_of_sale_3} монет')
                        else:
                            print('У тебя нет этого предмета, а потому ты, извинившись перед немного рассерженным торговцем уходишь обратно к фонтану.')
                    if action_7==4:
                        if inventory_name_4 in player['inventory']:
                            number_of_sale_4=player['inventory'].count('Порванный саван Бога Смерти Яропанага')
                            for i in range(number_of_sale_4):
                                player['inventory'].remove('Порванный саван Бога Смерти Яропанага')
                                player['money']+=2500
                            print(f'Торговец забирает у тебя {number_of_sale_4} Порванный саван Бога Смерти Яропанага и даёт тебе за него 2500*{number_of_sale_4} монет')
                        else:
                            print('У тебя нет этого предмета, а потому ты, извинившись перед немного рассерженным торговцем уходишь обратно к фонтану.')
                else:
                    print('Ты спокойно уходишь с рынка и возвращаешься к фонтану.')
                    sleep(3)
            if action_5==3:
                print('Ты приходишь к зданию алхимиков, ребят весёлых, с очень опасными зельями. Проходя в здания алхимиков, ты видишь стойку, а рядом с ней табличку с расценками, из которых тебя заинтересовало только несколько позициий:')
                sleep(3)
                print('Увеличение здоровья - 1000 монет (+100 здоровья). Каждое последующее усиление увеличивает цену на 1000 монет')
                print(f'Текущая цена:1000*{prise_6} монет')
                sleep(2)
                print('Увеличение силы - 1000 монет (+ 1 урон). Каждое последующее усиление увеличивает цену на 1000 монет.')
                print('(Использовать только после улучшения оружия до максимума)')
                print(f'Текущая цена:1000*{prise_8} монет')
                sleep(2)
                print('Увеличениие крепости тела - 1000 монет (-0.10 брони). Каждое последующее усиление увеличивает цену на 1000 монет (дополнительный модификатор брони). (Не более 5 раз)')
                print(f'Текущая цена:1000*{prise_7} монет')
                sleep(2)
                print('Желаешь ли ты пройти усиление?')
                action_8=int(input('Да(1)/Нет(2):'))
                if action_8==1:
                    action_9=int(input('Усиление чего ты хочешь пройти? Здоровья(1)/Силы(2)/Крепости(3)? '))
                    if action_9==1:
                        if player['money']>=1000*prise_6:
                            print('Ты проходишь неимоверно болезненную процедуру усиления, в ходе которой твое тело претерпевает изменения и ты явно становишься выносливее.')
                            player['hp']+=100
                            player['money']-=1000*prise_6
                            prise_6+=1
                            print(player['hp'])
                            sleep(3)
                        else:
                            print('Алхимики посмотрели на тебя, на твой пустой кошелёк надменно и усмехнувшись выставили тебя вон')
                            sleep(3)
                    if action_9==2:
                        if player['attack']>=15:
                            if player['money']>=1000*prise_7:
                                print('Ты проходишь неимоверно болезненную процедуру усиления, в ходе которой твое тело претерпевает изменения и ты явно становишься сильнее.')
                                player['attack']+=1
                                player['money']-=1000*prise_7
                                prise_7+=1
                                print(player['attack'])
                                sleep(3)
                            else:
                                print('Алхимики посмотрели на тебя, на твой пустой кошелёк и надменно усмехнувшись выставили тебя вон')
                                sleep(3)
                        else:
                            print('Алхимики сказали тебе, что не усиливают тех, кто ещё не улучшил своё оружие до максимума')
                            print('Тебе ничего не остаётся, кроме как вернуться к фонтану.')
                    if action_9==3:
                        if player['money']>=1000*prise_8:
                            if player['armor_dop']>=0.5:
                                print('Ты проходишь неимоверно болезненную процедуру усиления, в ходе которой твое тело претерпевает изменения и ты явно становишься прочнее.')
                                player['armor_dop']-=0.10
                                player['money']-=1000*prise_8
                                prise_8+=1
                                print(player['armor_dop'])
                                sleep(3)
                            else:
                                print('Алхимики говорят, что больше не могу усилить прочность твоуго тела, а потому, тебе ничего больше не остаётся, кроме как вернуться к фонтану')
                        else:
                            print('Алхимики посмотрели на тебя, на твой пустой кошелёк и надменно усмехнувшись выставили тебя вон')
                            sleep(3)
            if action_5==4:
                print('Ты заходишь в шатёр известного на весь город закленателя Робаута.')
                sleep(2)
                print('Он предлагает множество разнообразных услуг, но тебя привлекает только одна:')
                sleep(2)
                print(f'Увеличчение удачи:2000*{sell_luck} монет (не более 3 раз)')
                sleep(2)
                action_luck=int(input('Желаешь ли ты увеличить свою удачу? (Да(1)/Нет(2))'))
                if action_luck==1:
                    if player['luck']<=7:
                        if player['money']>=2000*sell_luck:
                            print('Робаут велит тебе лечь посередине шатра и после исполнения команды начинает расписывать вокруг тебя большой магический круг... После трёх часов, Робаут начинает произносить длинное заклинание, во время произношения которого ты начинаешь чувствовать, что внутри тебя что постепенно крепнет и увеличивается. После ещё трёх часов, Робаут прекращает читать заклинание и отпускает тебя прочь.')
                            player['money']-=2000*sell_luck
                            player['luck']+=1
                            sell_luck+=1
                            print(player['luck'])
                            sleep(3)
                        else:
                            print('Робаут прогоняет тебя, говоря о прохиндеях, которые не могут заплатить за выбранные услуги')
                            sleep(3)
                    else:
                        print('Робаут говорит, что не может ещё больше увеличить удачу и без того очень везучего человека. Тебе ничего не остаётся, кроме как вернться к фонтану.')
                        sleep(3)
                else:
                    print('Ты не решаешься увеличить свою удачу и спокойно возвращаешься к фонтану на главной площади.')
                    sleep(3)
        elif action==2:
            print('Ты выбираешь отправиться в леса на охоту, но на кого ты хочешь поохотиться?')
            sleep(2)
            print('Выбор здесь не очень велик: Слизь(1), Ликантроп(Опасно)(2), Отправиться к недавно найденной крипте(Очень Опасно)(3), Отправиться внутрь Крипты(СМЕРТЕЛЬНО!)(4), Отправиться в самые глубины Крипты(Конец)(5)')
            sleep(2)
            action_4=int(input('Что ты выбираешь?:'))
            if action_4==1:
                fight(0)
                sleep(3)
            elif action_4==2:
                fight(1)
                sleep(3)
            elif action_4==3:
                fight(2)
                sleep(3)
            elif action_4==4:
                fight(3)
                sleep(3)
            elif action_4==5:
                fight(4)
                sleep(3)
        elif action==3:
            print(player['inventory'])
            print(player['money'])
            sleep(3)
        elif action==4:
            print(f'Твой титул: {player["title"]}')
            print(f'Твоё имя: {player["name"]}')
            print(f'Твоя броня: {player["armor"]}')
            print(f'Твоя дополнительная броня: {player["armor_dop"]}')
            print(f'Твоё здоровье: {player["hp"]}')
            print(f'Твой урон: {player["attack"]}')
            print(f'Твоя удача: {player["luck"]}')
            sleep(3)