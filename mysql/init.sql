CREATE DATABASE IF NOT EXISTS nlp_db;

USE nlp_db;

CREATE TABLE IF NOT EXISTS news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT,
    content MEDIUMTEXT,
    font VARCHAR(255),
    publish_date DATETIME,
    processed BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS topics_entities (
    news_id INT PRIMARY KEY,
    topic INT,
    persons TEXT,
    organizations TEXT,
    locations TEXT,
    FOREIGN KEY (news_id) REFERENCES news(id)
);

CREATE TABLE IF NOT EXISTS labels (
    n_label INT PRIMARY KEY,
    name_label VARCHAR(255)
);

INSERT INTO labels (n_label, name_label) VALUES (-1, 'Temas_Generales_Vida');
INSERT INTO labels (n_label, name_label) VALUES (0, 'Vacunacion_COVID_Salud');
INSERT INTO labels (n_label, name_label) VALUES (1, 'Politica_EEUU_Elecciones');
INSERT INTO labels (n_label, name_label) VALUES (2, 'Futbol_Ingles_PremierLeague');
INSERT INTO labels (n_label, name_label) VALUES (3, 'Inmigracion_Frontera_EEUU');
INSERT INTO labels (n_label, name_label) VALUES (4, 'Violencia_Policial_Tiroteos');
INSERT INTO labels (n_label, name_label) VALUES (5, 'Conflicto_Afganistan_Taliban');
INSERT INTO labels (n_label, name_label) VALUES (6, 'Conflicto_Israel_Palestina');
INSERT INTO labels (n_label, name_label) VALUES (7, 'Control_Armas_Legislacion');
INSERT INTO labels (n_label, name_label) VALUES (8, 'Educacion_Universidad_Debates');
INSERT INTO labels (n_label, name_label) VALUES (9, 'Clima_Desastres_Naturales');
INSERT INTO labels (n_label, name_label) VALUES (10, 'Redes_Sociales_Tecnologia');
INSERT INTO labels (n_label, name_label) VALUES (11, 'Juegos_Olimpicos_Deportes');
INSERT INTO labels (n_label, name_label) VALUES (12, 'Cambio_Climatico_Energia');
INSERT INTO labels (n_label, name_label) VALUES (13, 'Medios_Noticias_Entrevistas');
INSERT INTO labels (n_label, name_label) VALUES (14, 'Consejos_Mascotas_Vida');
INSERT INTO labels (n_label, name_label) VALUES (15, 'Politica_Economia_ReinoUnido');
INSERT INTO labels (n_label, name_label) VALUES (16, 'Beisbol_Deportes_Chicago');
INSERT INTO labels (n_label, name_label) VALUES (17, 'Incendios_Forestales_California');
INSERT INTO labels (n_label, name_label) VALUES (18, 'Vida_Silvestre_Animales');
INSERT INTO labels (n_label, name_label) VALUES (19, 'Conflicto_Etiopia_Tigray');
INSERT INTO labels (n_label, name_label) VALUES (20, 'Finanzas_Negocios_ReinoUnido');
INSERT INTO labels (n_label, name_label) VALUES (21, 'NFL_Futbol_Americano');
INSERT INTO labels (n_label, name_label) VALUES (22, 'Golpe_Estado_Myanmar');
INSERT INTO labels (n_label, name_label) VALUES (23, 'Derecho_Aborto_EEUU');
INSERT INTO labels (n_label, name_label) VALUES (24, 'Crimen_Apunalamientos_RU');
INSERT INTO labels (n_label, name_label) VALUES (25, 'Musica_Albumes_Bandas');
INSERT INTO labels (n_label, name_label) VALUES (26, 'Criptomonedas_Bitcoin_Mercado');
INSERT INTO labels (n_label, name_label) VALUES (27, 'Conflicto_Rusia_Ucrania');
INSERT INTO labels (n_label, name_label) VALUES (28, 'Politica_Exterior_China');
INSERT INTO labels (n_label, name_label) VALUES (29, 'Acuerdo_Nuclear_Iran');
INSERT INTO labels (n_label, name_label) VALUES (30, 'Abuso_Sexual_Epstein_Maxwell');
INSERT INTO labels (n_label, name_label) VALUES (31, 'Terminos_Servicio_Online');
INSERT INTO labels (n_label, name_label) VALUES (32, 'Cricket_Inglaterra_Internacional');
INSERT INTO labels (n_label, name_label) VALUES (33, 'Politica_Latinoamerica_Crisis');
INSERT INTO labels (n_label, name_label) VALUES (34, 'Colapso_Edificio_Florida');
INSERT INTO labels (n_label, name_label) VALUES (35, 'Vehiculos_Electricos_Tesla');
INSERT INTO labels (n_label, name_label) VALUES (36, 'Cine_Peliculas_Hollywood');
INSERT INTO labels (n_label, name_label) VALUES (37, 'Economia_Inflacion_Empleo');
INSERT INTO labels (n_label, name_label) VALUES (38, 'Escandalo_Cuomo_Acoso');
INSERT INTO labels (n_label, name_label) VALUES (39, 'Juicio_Kyle_Rittenhouse');
INSERT INTO labels (n_label, name_label) VALUES (40, 'Corea_Norte_Nuclear_Misiles');
INSERT INTO labels (n_label, name_label) VALUES (41, 'Veteranos_Militares_Honor');
INSERT INTO labels (n_label, name_label) VALUES (42, 'Celebridades_Realeza_Escandalos');
INSERT INTO labels (n_label, name_label) VALUES (43, 'Religion_Cristianismo_Fe');
INSERT INTO labels (n_label, name_label) VALUES (44, 'Politica_India_Conflictos');
INSERT INTO labels (n_label, name_label) VALUES (45, 'Exploracion_Espacial_NASA');
INSERT INTO labels (n_label, name_label) VALUES (46, 'Educacion_Escolar_Debates');
INSERT INTO labels (n_label, name_label) VALUES (47, 'Moda_Belleza_Celebridades');
INSERT INTO labels (n_label, name_label) VALUES (48, 'Compras_Ofertas_Online');
INSERT INTO labels (n_label, name_label) VALUES (49, 'Recall_Gobernador_California');
INSERT INTO labels (n_label, name_label) VALUES (50, 'Tenis_Grand_Slams');
INSERT INTO labels (n_label, name_label) VALUES (51, 'Crimen_Robos_Violencia');
INSERT INTO labels (n_label, name_label) VALUES (52, 'Salud_Enfermedades_Tratamientos');
INSERT INTO labels (n_label, name_label) VALUES (53, 'Astrologia_Predicciones_Diarias');
INSERT INTO labels (n_label, name_label) VALUES (54, 'Cocina_Recetas_Comida');
INSERT INTO labels (n_label, name_label) VALUES (55, 'Accidentes_Trafico_Fatales');
INSERT INTO labels (n_label, name_label) VALUES (56, 'Sistema_Judicial_CorteSuprema');
INSERT INTO labels (n_label, name_label) VALUES (57, 'Oposicion_Rusia_Bielorrusia');
INSERT INTO labels (n_label, name_label) VALUES (58, 'Caso_Gabby_Petito_Desaparicion');
INSERT INTO labels (n_label, name_label) VALUES (59, 'Iglesia_Catolica_Vaticano');
INSERT INTO labels (n_label, name_label) VALUES (60, 'Realeza_Britanica_Eventos');
INSERT INTO labels (n_label, name_label) VALUES (61, 'Terrorismo_Francia_Europa');
INSERT INTO labels (n_label, name_label) VALUES (62, 'Television_RU_Espectaculos');
INSERT INTO labels (n_label, name_label) VALUES (63, 'Ciberseguridad_Ataques_Ransomware');
INSERT INTO labels (n_label, name_label) VALUES (64, 'Violencia_Genero_RU_Policia');
INSERT INTO labels (n_label, name_label) VALUES (65, 'Origenes_COVID19_Wuhan');
INSERT INTO labels (n_label, name_label) VALUES (66, 'Crisis_Migratoria_CanalMancha');
INSERT INTO labels (n_label, name_label) VALUES (67, 'Vivienda_Desalojos_Alquiler');
INSERT INTO labels (n_label, name_label) VALUES (68, 'Astronomia_Espacio_Universo');
INSERT INTO labels (n_label, name_label) VALUES (69, 'Tecnologia_Inalambrica_Salud');
INSERT INTO labels (n_label, name_label) VALUES (70, 'Pena_Muerte_Ejecuciones');
INSERT INTO labels (n_label, name_label) VALUES (71, 'Entrevistas_Politicas_CBS');
INSERT INTO labels (n_label, name_label) VALUES (72, 'Politica_Brasil_Bolsonaro');
INSERT INTO labels (n_label, name_label) VALUES (73, 'Hong_Kong_Prodemocracia_China');
INSERT INTO labels (n_label, name_label) VALUES (74, 'Noticias_CBS_Titulares');
INSERT INTO labels (n_label, name_label) VALUES (75, 'Legalizacion_Cannabis_Drogas');
INSERT INTO labels (n_label, name_label) VALUES (76, 'Deportes_Universitarios_Resultados');
INSERT INTO labels (n_label, name_label) VALUES (77, 'Deuda_Estudiantil_Educacion');
INSERT INTO labels (n_label, name_label) VALUES (78, 'Formula1_Automovilismo_Competicion');
INSERT INTO labels (n_label, name_label) VALUES (79, 'Tensiones_Taiwan_China_Militar');
INSERT INTO labels (n_label, name_label) VALUES (80, 'Urbanismo_Chicago_Comunidad');
INSERT INTO labels (n_label, name_label) VALUES (81, 'Sindicalismo_Amazon_Trabajadores');
INSERT INTO labels (n_label, name_label) VALUES (82, 'Brexit_RU_UE_Irlanda');
INSERT INTO labels (n_label, name_label) VALUES (83, 'Escandalo_Matt_Gaetz_Congreso');
INSERT INTO labels (n_label, name_label) VALUES (84, 'Crisis_Opiaceos_Drogas_FDA');
INSERT INTO labels (n_label, name_label) VALUES (85, 'Viajes_Aerolineas_Cancelaciones');
INSERT INTO labels (n_label, name_label) VALUES (86, 'Politica_Africana_Lideres');
INSERT INTO labels (n_label, name_label) VALUES (87, 'Mercado_Acciones_Gamestop');
INSERT INTO labels (n_label, name_label) VALUES (88, 'Monumentos_Confederados_Debate');
INSERT INTO labels (n_label, name_label) VALUES (89, 'Crimenes_Odio_Racismo_EEUU');
INSERT INTO labels (n_label, name_label) VALUES (90, 'Cuba_Protestas_Comunismo');
INSERT INTO labels (n_label, name_label) VALUES (91, 'NBA_Baloncesto_Jugadores');
INSERT INTO labels (n_label, name_label) VALUES (92, 'Erupciones_Volcanicas_Desastres');
INSERT INTO labels (n_label, name_label) VALUES (93, 'Defensa_Militar_EEUU_Pentagono');
INSERT INTO labels (n_label, name_label) VALUES (94, 'Mercado_Bursatil_Inversiones');
INSERT INTO labels (n_label, name_label) VALUES (95, 'Crisis_Libano_Beirut_Explosion');
INSERT INTO labels (n_label, name_label) VALUES (96, 'Deuda_Publica_EEUU_Congreso');
INSERT INTO labels (n_label, name_label) VALUES (97, 'Politica_Turquia_Internacional');
INSERT INTO labels (n_label, name_label) VALUES (98, 'Politica_Filipinas_Duterte');
INSERT INTO labels (n_label, name_label) VALUES (99, 'Autismo_Discapacidad_Infancia');
INSERT INTO labels (n_label, name_label) VALUES (100, 'Abuso_Sexual_Celebridades_Musica');
INSERT INTO labels (n_label, name_label) VALUES (101, 'Juicio_Ahmaud_Arbery_Asesinato');
INSERT INTO labels (n_label, name_label) VALUES (102, 'Golf_PGA_Torneos');
INSERT INTO labels (n_label, name_label) VALUES (103, 'Apuestas_Deportivas_Casinos');
INSERT INTO labels (n_label, name_label) VALUES (104, 'Accidentes_Aereos_Investigacion');
INSERT INTO labels (n_label, name_label) VALUES (105, 'Arqueologia_Egipto_Antiguo');
INSERT INTO labels (n_label, name_label) VALUES (106, 'Fraude_Financiero_Legal');
INSERT INTO labels (n_label, name_label) VALUES (107, 'Oleoductos_Energia_MedioAmbiente');
INSERT INTO labels (n_label, name_label) VALUES (108, 'Clima_Nieve_Invierno_Chicago');
INSERT INTO labels (n_label, name_label) VALUES (109, 'Boxeo_MMA_Peleas');
INSERT INTO labels (n_label, name_label) VALUES (110, 'Precios_Petroleo_Gasolina');
INSERT INTO labels (n_label, name_label) VALUES (111, 'Reserva_Federal_Economia_EEUU');
INSERT INTO labels (n_label, name_label) VALUES (112, 'Transporte_Publico_Londres');
INSERT INTO labels (n_label, name_label) VALUES (113, 'Alcaldia_Chicago_PoliticaLocal');
INSERT INTO labels (n_label, name_label) VALUES (114, 'Politica_Alemania_Merkel');
INSERT INTO labels (n_label, name_label) VALUES (115, 'Embarazo_Maternidad_Salud');
INSERT INTO labels (n_label, name_label) VALUES (116, 'Conflicto_Nigeria_Secuestros');
INSERT INTO labels (n_label, name_label) VALUES (117, 'Premios_Cine_Espectaculo');
INSERT INTO labels (n_label, name_label) VALUES (118, 'Politica_Israel_Gobierno');
INSERT INTO labels (n_label, name_label) VALUES (119, 'Presupuesto_Estatal_CarolinaNorte');
INSERT INTO labels (n_label, name_label) VALUES (120, 'Escasez_Conductores_Combustible_RU');
INSERT INTO labels (n_label, name_label) VALUES (121, 'Sueno_Descanso_Salud');
INSERT INTO labels (n_label, name_label) VALUES (122, 'Incidentes_Vuelos_Pasajeros');
INSERT INTO labels (n_label, name_label) VALUES (123, 'Servicio_Postal_EEUU_USPS');
INSERT INTO labels (n_label, name_label) VALUES (124, 'Canal_Suez_Bloqueo_Barcos');
INSERT INTO labels (n_label, name_label) VALUES (125, 'Impuestos_Reforma_Fiscal_EEUU');
INSERT INTO labels (n_label, name_label) VALUES (126, 'Desinformacion_Pensamiento_Critico');
INSERT INTO labels (n_label, name_label) VALUES (127, 'Derrames_Petroleo_Contaminacion');
INSERT INTO labels (n_label, name_label) VALUES (128, 'Arte_Museos_Exposiciones');
INSERT INTO labels (n_label, name_label) VALUES (129, 'Desaparicion_Vuelos_Malasia');
INSERT INTO labels (n_label, name_label) VALUES (130, 'Crisis_Agua_Flint_Michigan');
INSERT INTO labels (n_label, name_label) VALUES (131, 'Tecnologia_Militar_Aeronautica');
INSERT INTO labels (n_label, name_label) VALUES (132, 'Negocios_Trump_Propiedades');
INSERT INTO labels (n_label, name_label) VALUES (133, 'Vicepresidencia_EEUU_KamalaHarris');
INSERT INTO labels (n_label, name_label) VALUES (134, 'Salario_Minimo_Trabajadores');
INSERT INTO labels (n_label, name_label) VALUES (135, 'Reconocimiento_Facial_Privacidad');
INSERT INTO labels (n_label, name_label) VALUES (136, 'Carreras_Caballos_Controversia');
INSERT INTO labels (n_label, name_label) VALUES (137, 'Festivales_Artes_Escenicas');
INSERT INTO labels (n_label, name_label) VALUES (138, 'Narcotrafico_Drogas_DEA');
INSERT INTO labels (n_label, name_label) VALUES (139, 'Estadisticas_Globales_Pandemia');
INSERT INTO labels (n_label, name_label) VALUES (140, 'Virus_Zika_Mosquitos_Salud');
INSERT INTO labels (n_label, name_label) VALUES (141, 'Exploracion_Marte_NASA_Rover');
INSERT INTO labels (n_label, name_label) VALUES (142, 'Crisis_Cadena_Suministro_Puertos');
INSERT INTO labels (n_label, name_label) VALUES (143, 'Accidentes_Parques_Acuaticos');
INSERT INTO labels (n_label, name_label) VALUES (144, 'Festividades_EEUU_Historia');
INSERT INTO labels (n_label, name_label) VALUES (145, 'Assange_Wikileaks_Extradicion');
INSERT INTO labels (n_label, name_label) VALUES (146, 'Sistema_Penitenciario_Prisiones');
INSERT INTO labels (n_label, name_label) VALUES (147, 'Politica_Illinois_Corrupcion');
INSERT INTO labels (n_label, name_label) VALUES (148, 'Desarrollo_Urbano_RU_Ciudades');
INSERT INTO labels (n_label, name_label) VALUES (149, 'Hunter_Biden_Controversia_Arte');
INSERT INTO labels (n_label, name_label) VALUES (150, 'Inteligencia_Seguridad_CIA_FBI');
INSERT INTO labels (n_label, name_label) VALUES (151, 'Crimen_Investigacion_Television');
INSERT INTO labels (n_label, name_label) VALUES (152, 'Elecciones_Alcaldia_NuevaYork');
INSERT INTO labels (n_label, name_label) VALUES (153, 'Politica_Texas_Republicanos');
INSERT INTO labels (n_label, name_label) VALUES (154, 'Filantropia_Fundaciones_Diversidad');
INSERT INTO labels (n_label, name_label) VALUES (155, 'Baile_Television_BBC_Strictly');
INSERT INTO labels (n_label, name_label) VALUES (156, 'Crisis_Fronteriza_Bielorrusia_Polonia');
INSERT INTO labels (n_label, name_label) VALUES (157, 'Personas_Desaparecidas_Policia');
INSERT INTO labels (n_label, name_label) VALUES (158, 'Libros_Literatura_Autores');
INSERT INTO labels (n_label, name_label) VALUES (159, 'Caso_Jussie_Smollett_Engano');
INSERT INTO labels (n_label, name_label) VALUES (160, 'Naufragios_Rescates_Guardacostas');
INSERT INTO labels (n_label, name_label) VALUES (161, 'Transplantes_Organos_Medicina');
INSERT INTO labels (n_label, name_label) VALUES (162, 'Bebidas_Alcoholicas_Produccion');
INSERT INTO labels (n_label, name_label) VALUES (163, 'Fallecimientos_Actores_Television');
INSERT INTO labels (n_label, name_label) VALUES (164, 'Financiamiento_Politico_Corporaciones');
INSERT INTO labels (n_label, name_label) VALUES (165, 'Spyware_Pegasus_Vigilancia');
INSERT INTO labels (n_label, name_label) VALUES (166, 'Olas_Calor_Clima_Extremo');
INSERT INTO labels (n_label, name_label) VALUES (167, 'Abuso_Sexual_Institucional');
INSERT INTO labels (n_label, name_label) VALUES (168, 'Empresas_Chinas_Regulacion');
INSERT INTO labels (n_label, name_label) VALUES (169, 'Seguro_Salud_EEUU_Reforma');
INSERT INTO labels (n_label, name_label) VALUES (170, 'Alpinismo_Desastres_Montanas');
INSERT INTO labels (n_label, name_label) VALUES (171, 'Periodismo_Etica_Correcciones');