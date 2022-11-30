INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (1, 'hurensohn', 'hurensohn@gmail.com', 123, 'DHBW', 'Hurensohn GMBH', 'w');
INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (2, 'benestinkt', 'benestinkt@hurensohn.de', 12, 'Uni Saarland',
        'Bene ist wirklich dumm wie Brot und weiß gar nichts', 'm');
INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (3, 'meriberi', 'meriberi@fauxia.de', 20, 'DHBW', 'Meri ist einfach krass kuhl.', 'd');
INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (4, 'flippydippy', 'FilB00yyyy@gmail.com', 20, 'DHBW', 'Hier kommt Flipper! ', 'm');
INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (5, 'Fr3shDumb1ed0r', 'MaxiFlöte@email.com', 20, 'MIT', 'Back from the underground, back for more!', 'm');
INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (6, 'kirrlachkev', 'kevin@kernsdrohnenfo', 20, 'KIT', 'BWL Tipps mit Kevin', 'm');
INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (7, 'sopjoto', 'sophie@trottel.com', 18, 'DHBW', 'Im Pferdeglück', 'w');
INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (8, 'guenther_jauch', 'guenther@einemillion', 42, 'RTL', 'Wollen Sie den Telefonjoker anrufen?', 'x');
INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (9, 'baukloetzchen', 'logik@schwinni.com', 73, 'DHBW Stuttgart', 'Pfeiler...', 'x');
INSERT INTO start_user (user_id, username, user_email, user_age, university, user_bio, gender)
VALUES (10, 'salzrocks', 'jaman@salzrocks.de', 420, 'TU Kaiserslautern', 'JA MANN!! SALZ!!!', 'd');
INSERT INTO start_tag (id, value)
VALUES (1, 'BeneStinkt');
INSERT INTO start_tag (id, value)
VALUES (2, 'wandern');
INSERT INTO start_tag (id, value)
VALUES (3, 'schwimmen');
INSERT INTO start_tag (id, value)
VALUES (4, 'koksen');
INSERT INTO start_tag (id, value)
VALUES (5, 'trinken');
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (1, '1652757626000', '1652757630000', 'Mannheim', 'Übernachtungsparty in Mannheim', 'Schlaflos in Mannheim', 1,
        1, 5);
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (2, '1652757626000', '1652757630000', 'Bayern', 'Wir raiden Bayern und schlachten alle ab', 'Bayern-Raid', 2, 0,
        5);
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (3, '1652757626000', '1652757630000', 'Mars', 'Der Mars gehört jetzt uns hehe', 'Mars Invasion', 3, 0, 5);
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (4, '1652757626000', '1652757630000', 'Mannheim', 'Wir saufen bis nachts um 4', 'Saufen', 4, 1, 5);
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (5, '1652757626000', '1652757630000', 'Berlin', 'Es ist Zeit für den Neuanfang', 'Bundesregierung stürzen', 5, 0,
        5);
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (6, '1652757626000', '1652757630000', 'Saarland', 'Selbsterklärend.', 'SweetHomeAlabama', 6, 1, 5);
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (7, '1652757626000', '1652757630000', 'Pfalz', 'Annerstwo ist annerst und halt net wie in da palz!', 'Pfalzkind',
        7, 0, 5);
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (8, '1652757626000', '1652757630000', 'DHBW', 'Spaß für die ganze Familie', 'Vorlesung', 8, 1, 5);
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (9, '1652757626000', '1652757630000', 'Stuttgart', 'return of the Blöcke', 'Searching for schwinn', 9, 1, 5);
INSERT INTO start_event (id, date_published, date, location, description, title, creator_id, is_private, member_limit)
VALUES (10, '1652757626000', '1652757630000', 'München',
        'Wir hatten einen Termin? Ich muss leider Spontan nach München!', 'Spontan nach München', 10, 0, 5);
