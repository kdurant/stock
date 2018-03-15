#-*- coding:utf-8 -*-
import tushare as ts
import numpy as np
import time
id = [
    '000825', '600249', '000795', '000151', '002208', '300655', '300523', '603506'
    , '300732', '600405', '300647', '603712', '300731', '300688', '002922', '300490', '000672', '002853', '002629', '600801', '002596', '603778', '601636', '300737', '300104', '000789', '300727', '002687', '600802', '603680', '300643', '600962', '603081', '600322', '000885', '603916', '002923', '300733', '603180', '603269', '002074', '002928', '002428', '002084', '300477', '600766', '603688', '300611', '300619', '600585', '002171', '603605', '600727', '002053', '600207', '600740', '002066', '603619', '002382', '600635', '002919', '300689', '603758', '600209', '603367', '002791', '600392', '002718', '600782', '600182', '300231', '600992', '002136', '000568', '000903', '002611', '603059', '002286', '002658', '300462', '002915', '603110', '002004', '002320', '300623', '300721', '600623', '002233', '002289', '000636', '603977', '300272', '601500', '002480', '000735', '000673', '603917', '603617', '000936', '600387',
    '600019', '300151', '000687', '000856', '600462', '002632', '600111', '600783', '600985', '002162', '600439', '000585', '002472', '000935', '603069', '002901', '002625', '002290', '601012', '002073', '300717', '002485', '600720', '300160', '603960', '002906', '600561', '600596', '002685', '002921', '600398', '603136', '300099', '002056', '000953', '603458', '002116', '603779', '603589', '600769', '002189', '002127', '603161', '300507', '300559', '002633', '002716', '300526', '002057', '603717', '600297', '601226', '000717', '603181', '300678', '002861', '000970', '000932', '002867', '603709', '002725', '002565', '002753', '002016', '600449', '000603', '002284', '002601', '600519', '002278', '600549', '601899', '603809', '600095', '002841', '601188', '002631', '600248', '002860', '603858', '300257', '000993', '002918', '300735', '300511', '601699', '000532', '600965', '002742', '603333', '000895', '603878', '000546', '601600', '603727', '001979', '002828', '603321', '000537',
    '603909', '600883', '002110', '002202', '000752', '300716', '300740', '600486', '600668', '002873', '002782', '002109', '601828', '000586', '600771', '600970', '600722', '002669', '000898', '603711', '000401', '002160', '603040', '603848', '600116', '300398', '600146', '300591', '603123', '300637', '000403', '002903', '600903', '000886', '601113', '603429', '002230', '000797', '600497', '000813', '600741', '002239', '300664', '600980', '300703', '603233', '600215', '000517', '300680', '002809', '600219', '600362', '002209', '002077', '600507', '601888', '600295', '600976', '600276', '600809', '600383', '000825', '000831', '300164', '601608', '600715', '002508', '002801', '300729', '603085', '600580', '603787', '601388', '300127', '600606', '000877', '300051', '300713', '600188', '300065', '000848', '000858', '300602', '002356', '002377', '600728', '601005', '600243', '002457', '600779', '601811', '002889', '002845', '002352', '603959', '300697', '600229', '601808', '002007',
    '000720', '300650', '600702', '002459', '300125', '300149', '300003', '002929', '002717', '000596', '600331', '002199', '002734', '603595', '600529', '601611', '600566', '600881', '000713', '600569', '603776', '000906', '600355', '002227', '600678', '002812', '000761', '600936', '002813', '000987', '000631', '300741', '600583', '300322', '600366', '601016', '000927', '000810', '300497', '603637', '000410', '300374', '600126', '002134', '600348', '600687', '000610', '600130', '002469', '300726', '603225', '002883', '002740', '600763', '002092', '002778', '601003', '601225', '300529', '002276', '002652', '603357', '600131', '600259', '300191', '603612', '002910', '002304', '002091', '600858', '000786', '600191', '600028', '600282', '002478', '000605', '603580', '300363', '601992', '600368', '600053', '600326', '600138', '603722', '000012', '601155', '002603', '300501', '300059', '002383', '002145', '000878', '600011', '300649', '002107', '002262', '002008', '603639', '000708',
    '300712', '002228', '601801', '002150', '002927', '603658', '300575', '603519', '600874', '600225', '000791', '002850', '000002', '603533', '002086', '601118', '601001', '002028', '002391', '300695', '601666', '601727', '002032', '603080', '300001', '002258', '002898', '600674', '603598', '601011', '600559', '600210', '000059', '002196', '603882', '000999', '300279', '002646', '002626', '603980', '300686', '600528', '000909', '002674', '000933', '300666', '601015', '600691', '603035', '000952', '002673', '300657', '603685', '000023', '603133', '603316', '002018', '600547', '600321', '600483', '002706', '603183', '601021', '300595', '600184', '600636', '603326', '603156', '600351', '002403', '002117', '600242', '002701', '603169', '000837', '601088', '300710', '600618', '600792', '002664', '603197', '603527', '002019', '002021', '002204', '300587', '603721', '002482', '000758', '600216', '603100', '002865', '601677', '600176', '300635', '002909', '002884', '600367', '000633',
    '002141', '300243', '603117', '600114', '603699', '002597', '603609', '600871', '600231', '600010', '002578', '002531', '600156', '600830', '600645', '000890', '002395', '000554', '300642', '603050', '600577', '002518', '600660', '601601', '603801', '300558', '002859', '601168', '600516', '000060', '600466', '600293', '300422', '002848', '000626', '000729', '601101', '002064', '601311', '603517', '000524', '002858', '300376', '000788', '600664', '600389', '603289', '300214', '603368', '300136', '600123', '600062', '000807', '002926', '000799', '600803', '000488', '603278', '603866', '600795', '603788', '000818', '600346', '300371', '603018', '603500', '603829', '002393', '601127', '000931', '603335', '300035', '002237', '002167', '600531', '000989', '000601', '600744', '603365', '603331', '600096', '000922', '600048', '600425', '002683', '603167', '000550', '603668', '000709', '603661', '002216', '002229', '600833', '600608', '002182', '300218', '600551', '002114', '000055',
    '600808', '600508', '002390', '000005', '300580', '600555', '600859', '601336', '600037', '603708', '002614', '600311', '000036', '002479', '002248', '603976', '600546', '002125', '000751', '002887', '600491', '600892', '600335', '002769', '002128', '600887', '000869', '601933', '600180', '002010', '300335', '600196', '002678', '002146', '600986', '002426', '600320', '300141', '000959', '000923', '600535', '000657', '300120', '300118', '600736', '002671', '603303', '600816', '603890', '002491', '603730', '601117', '603038', '300393', '600639', '600600', '600021', '002349', '603686', '600280', '002680', '600707', '600273', '002369', '603616', '002407', '002245', '000526', '300534', '002881', '300330', '002522', '600971', '002094', '300281', '002317', '300668', '603922', '600641', '600160', '600621', '600933', '300482', '300387', '603599', '002741', '600233', '300285', '603859', '300632', '603888', '300180', '603507', '600754', '603079', '600436', '603998', '603955', '603919',
    '603887', '603885', '603843', '603822', '603799', '603725', '603718', '603696', '603690', '603667', '603659', '603636', '603603', '603538', '603520', '603508', '603398', '603393', '603377', '603318', '603309', '603308', '603222', '603066', '603033', '603032', '603021', '601898', '601857', '601619', '601519', '601216', '601158', '601099', '600997', '600987', '600960', '600900', '600880', '600877', '600875', '600870', '600866', '600856', '600825', '600807', '600798', '600794', '600784', '600777', '600753', '600751', '600735', '600734', '600733', '600711', '600710', '600701', '600685', '600682', '600666', '600647', '600629', '600614', '600581', '600568', '600567', '600557', '600539', '600515', '600512', '600489', '600485', '600423', '600401', '600399', '600395', '600393', '600378', '600365', '600309', '600306', '600290', '600270', '600257', '600255', '600241', '600228', '600226', '600221', '600217', '600187', '600179', '600165', '600157', '600150', '600148', '600145', '600122',
    '600117', '600086', '600084', '600076', '600069', '600054', '600051', '600022', '300700', '300682', '300670', '300662', '300659', '300656', '300640', '300634', '300624', '300593', '300586', '300578', '300491', '300470', '300464', '300457', '300455', '300444', '300441', '300424', '300411', '300410', '300409', '300392', '300390', '300383', '300356', '300341', '300337', '300325', '300321', '300317', '300312', '300309', '300290', '300280', '300278', '300266', '300240', '300238', '300237', '300225', '300198', '300173', '300165', '300159', '300156', '300146', '300134', '300128', '300116', '300103', '300090', '300089', '300086', '300071', '300067', '300064', '300056', '300049', '300041', '300038', '300032', '300004', '002930', '002870', '002866', '002857', '002851', '002799', '002770', '002765', '002739', '002738', '002726', '002721', '002699', '002694', '002692', '002662', '002661', '002656', '002655', '002650', '002647', '002622', '002619', '002617', '002613', '002607', '002604',
    '002592', '002586', '002584', '002580', '002575', '002552', '002545', '002538', '002532', '002524', '002523', '002520', '002515', '002509', '002507', '002490', '002475', '002464', '002451', '002450', '002447', '002442', '002440', '002438', '002437', '002427', '002423', '002413', '002409', '002398', '002384', '002366', '002363', '002357', '002345', '002341', '002321', '002312', '002310', '002309', '002301', '002263', '002260', '002259', '002256', '002252', '002249', '002244', '002219', '002213', '002212', '002210', '002201', '002198', '002184', '002168', '002163', '002161', '002147', '002143', '002137', '002122', '002121', '002113', '002103', '002098', '002090', '002085', '002082', '002075', '002072', '002047', '002034', '002005', '001696', '000998', '000985', '000983', '000979', '000972', '000969', '000962', '000960', '000958', '000949', '000939', '000930', '000912', '000900', '000820', '000812', '000796', '000793', '000766', '000757', '000731', '000703', '000693', '000688',
    '000666', '000663', '000630', '000616', '000613', '000606', '000566', '000564', '000555', '000547', '000545', '000540', '000534', '000533', '000516', '000509', '000506', '000419', '000415', '000156', '000069', '000056', '000046', '000038', '000035', '000034', '000031', '000029', '000022', '000019', '300651', '300654', '002359', '603165', '600697', '300037', '603655', '002080', '002746', '000503', '600083', '600977', '002193', '000408', '002871', '603638', '002039', '603055', '002589', '002353', '603288', '300636', '002488', '300429', '300269', '000968', '002920', '601111', '603200', '002895', '603569', '002691', '603608', '603196', '601678', '000732', '600328', '600409', '000528', '300015', '002521', '000418', '600284', '601163', '600330', '601886', '600548', '600240', '000976', '000690', '603369', '603676', '603630', '002373', '002414', '002319', '002293', '603076', '600909', '600104', '600094', '300008', '603566', '002666', '002654', '600161', '002002', '600502', '000955',
    '300459', '603223', '002468', '600478', '300174', '002775', '002067', '600333', '603179', '002863', '600706', '002899', '002452', '600860', '603963', '600688', '000725', '300517', '600277', '300196', '002811', '002120', '603139', '603996', '600026', '600227', '600657', '600082', '000937', '002240', '000426', '600332', '600079', '300401', '002663', '601199', '000423', '000166', '603898', '600873', '600175', '600091', '002454', '600345', '000043', '300569', '600595', '000929', '002144', '600540', '000822', '000590', '002365', '000990', '600586', '601618', '601028', '000429', '603386', '000917', '002542', '002908', '002499', '603488', '600815', '600959', '600661', '600638', '300519', '603226', '603003', '002097', '600759', '600223', '600829', '300500', '600693', '000008', '000552', '002336', '002183', '600886', '000828', '601211', '600033', '603029', '603299', '601878', '603388', '600308', '002541', '000897', '002864', '603359', '603009', '002205', '002825', '603345', '603477',
    '601515', '002749', '002445', '603568', '600285', '002460', '002805', '603260', '002635', '600015', '000049', '600848', '600966', '002723', '603380', '600556', '002394', '600350', '002203', '300224', '600503', '603027', '300547', '300400', '002672', '002191', '000541', '603116', '600236', '002155', '600315', '601555', '002327', '002516', '002559', '300072', '000338', '002566', '002412', '601368', '002840', '600714', '002422', '600325', '300683', '600307', '002324', '600305', '002102', '000417', '002330', '600283', '002842', '002280', '300132', '600979', '603555', '600712', '000888', '600599', '000611', '603663', '000155', '000600', '603968', '603086', '002055', '000615', '000400', '300270', '601985', '600708', '000028', '300530', '600422', '603737', '002051', '300739', '002872', '600604', '002761', '000539', '300185', '002547', '600369', '002234', '600597', '600110', '000557', '002088', '000682', '601006', '600984', '002044', '600239', '000652', '600550', '000755', '000096',
    '002628', '002511', '002587', '603985', '300153', '601901', '600747', '600729', '603026', '000157', '601328', '002294', '000833', '600780', '002665', '600605', '600821', '600127', '300221', '002484', '000016', '300550', '000671', '300658', '600499', '601988', '600438', '600509', '600888', '601107', '002108', '002888', '601108', '600648', '002660', '000430', '300408', '300450', '002890', '603396', '600663', '002100', '000513', '002571', '000911', '600961', '000027', '600501', '000635', '300396', '600538', '002648', '002386', '600170', '603515', '601966', '002372', '002737', '000576', '600683', '600121', '603178', '600201', '600522', '600764', '002736', '000860', '600470', '300189', '603798', '300239', '600089', '601019', '000762', '300583', '300620', '600738', '002378', '601668', '603728', '000736', '601900', '300513', '000918', '603738', '002893', '000963', '603063', '300660', '603665', '600327', '000778', '600064', '300485', '002519', '002337', '000899', '603880', '603766',
    '603089', '601918', '601518', '600781', '002905', '300522', '002318', '300669', '601098', '002630', '601717', '300294', '000780', '000099', '002307', '600804', '002711', '002679', '300435', '600827', '600269', '600594', '000538', '600377', '600433', '300069', '603860', '002441', '002186', '600203', '603383', '000975', '002653', '300626', '601866', '603856', '002536', '000525', '300615', '603166', '002268', '002756', '600169', '601928', '002397', '002868', '601369', '600381', '600390', '603556', '600271', '002686', '000750', '000667', '002015', '600208', '600837', '600403', '002803', '002033', '300582', '300081', '300533', '603606', '002563', '600919', '600812', '002627', '002434', '300087', '300563', '000803', '601628', '002003', '600318', '600080', '300553', '603701', '601882', '000402', '601881', '600843', '002466', '600642', '002600', '600726', '601169', '603444', '000715', '600206', '002461', '000510', '002462', '002540', '300613', '603889', '300478', '000739', '000416',
    '002715', '600300', '603518', '002111', '000090', '603869', '300070', '300616', '600023', '002333', '603585', '002281', '600158', '603028', '600025', '002530', '600199', '000563', '601229', '600007', '601377', '600141', '002564', '600058', '300618', '600303', '603229', '600260', '000686', '000925', '600299', '000926', '002745', '000514', '600800', '002206', '601375', '600252', '603466', '601020', '002557', '600823', '600872', '601991', '300641', '300355', '002612', '000776', '600901', '601177', '300375', '601566', '600098', '000150', '603157', '600563', '600090', '601908', '600386', '000727', '000598', '300091', '601233', '600882', '000783', '300483', '300328', '600000', '002797', '002453', '600268', '002042', '600461', '002267', '002370', '603618', '002443', '600853', '600611', '300010', '002705', '600695', '000625', '600743', '002585', '600487', '600020', '000413', '603729', '000001', '002527', '300545', '600340', '300006', '000726', '601669', '600078', '002483', '300117',
    '000913', '600031', '000587', '002634', '603989', '300014', '300472', '002225', '002577', '002250', '603228', '300403', '600418', '000159', '002495', '603966', '600479', '600847', '000592', '603378', '600262', '002550', '000880', '600287', '300202', '002126', '603833', '000581', '601318', '603777', '300301', '000951', '601238', '600582', '600339', '300351', '603937', '600988', '300029', '600406', '603322', '002014', '002500', '300082', '600723', '000422', '002643', '600543', '000668', '600510', '002882', '002024', '300033', '600129', '600814', '002876', '300054', '601998', '600895', '600177', '300145', '300195', '600680', '000965', '000875', '603238', '600035', '601009', '601339', '002038', '300702', '600493', '601218', '002534', '002815', '002502', '300137', '603816', '000685', '603008', '603600', '002288', '600742', '601398', '600615', '603768', '002165', '600690', '600109', '600993', '601818', '600649', '603421', '002347', '600189', '603881', '300652', '002435', '603757',
    '002727', '600684', '600016', '603577', '002837', '300488', '300119', '601877', '000792', '002346', '300711', '002847', '603389', '601633', '300382', '300206', '002730', '300365', '000921', '600008', '601288', '000961', '002602', '002788', '300709', '002501', '600999', '002802', '002498', '603337', '300289', '002878', '002682', '600375', '002379', '002061', '000863', '603899', '600429', '002591', '002496', '600151', '002187', '000802', '600819', '600982', '300129', '600190', '603567', '600291', '603131', '600329', '600168', '002151', '002796', '002533', '002071', '300106', '300475', '600787', '002621', '300548', '000404', '300736', '002178', '603199', '600861', '600739', '300217', '603501', '300193', '002792', '300130', '603997', '002174', '603558', '600112', '600820', '002170', '601929', '600017', '000876', '000683', '000428', '000100', '600628', '002567', '603906', '603315', '603839', '600884', '002537', '601186', '000523', '603660', '002059', '002192', '000798', '600575',
    '300158', '000777', '002148', '600863', '002582', '600865', '300172', '600400', '603818', '600496', '002561', '002411', '000910', '600067', '600183', '002037', '603579', '000851', '002149', '000607', '603060', '000333', '603908', '002029', '002724', '000407', '002620', '000411', '600376', '300596', '000680', '000883', '600488', '601595', '600658', '300048', '600699', '300094', '601996', '601689', '002043', '002142', '002806', '300576', '600036', '300590', '002421', '300169', '601018', '300672', '603826', '603002', '300181', '600380', '600061', '600050', '002385', '600996', '002060', '600824', '300163', '002311', '600060', '000612', '002001', '603129', '002703', '600197', '002639', '600963', '300705', '300554', '600426', '603939', '002254', '002387', '000697', '300420', '603036', '600246', '600724', '603823', '002821', '300233', '002402', '000728', '600135', '600652', '300479', '601788', '000089', '603001', '600748', '600500', '600059', '603043', '600793', '300283', '000966',
    '603767', '002287', '300068', '000632', '600665', '300508', '300286', '002449', '300080', '603535', '300308', '300108', '603601', '601179', '300220', '300621', '300425', '600452', '600004', '002731', '300625', '600323', '603208', '000573', '601390', '600876', '002747', '603607', '002101', '000559', '600106', '002562', '603198', '603677', '002164', '600790', '603886', '600212', '600897', '600388', '002408', '002681', '300667', '600363', '002221', '000498', '600773', '300437', '000830', '601789', '002027', '002159', '601872', '600969', '002099', '000967', '000504', '300617', '603000', '603536', '600894', '600601', '002497', '002012', '300178', '002917', '600370', '300058', '300100', '000531', '300327', '300026', '000698', '600587', '600552', '300570', '600719', '002285', '300260', '601989', '300228', '601919', '300062', '600767', '601258', '603879', '600085', '002833', '600521', '002773', '603012', '600926', '300395', '600266', '002374', '600103', '600637', '600039', '002608',
    '603090', '603339', '601969', '603037', '300415', '300622', '000505', '603268', '601166', '000553', '000691', '600757', '603277', '600235', '603358', '600572', '300229', '000063', '000695', '300645', '300096', '603726', '601949', '002083', '300699', '002820', '601799', '300020', '600279', '000826', '002302', '601139', '600027', '300665', '603020', '600030', '600758', '600725', '300358', '300360', '600312', '603991', '300075', '002902', '002433', '002068', '600785', '300320', '600397', '002050', '300432', '002535', '601688', '600983', '601106', '601939', '002911', '002020', '002417', '300039', '002455', '300273', '000037', '601010', '002752', '603311', '000529', '002512', '601616', '600132', '300379', '300718', '300648', '600136', '002179', '600167', '000718', '600356', '000892', '002139', '000650', '603920', '600468', '600159', '002243', '000065', '600995', '002719', '603098', '000623', '000850', '600694', '600009', '300107', '300255', '300258', '300423', '600713', '000501',
    '600864', '002549', '600220', '600885', '603077', '601002', '300204', '600192', '603979', '000009', '600958', '601126', '600143', '002298', '300199', '600826', '002816', '603160', '600455', '600675', '600396', '601007', '002554', '600185', '002732', '300135', '300498', '300168', '601766', '002817', '000767', '002048', '600172', '600481', '300126', '300083', '600746', '002798', '000661', '300438', '300274', '000737', '000809', '600844', '002514', '600063', '300353', '002410', '002197', '000973', '300262', '601997', '002404', '600705', '002493', '603912', '601968', '600448', '600419', '002096', '000719', '300439', '002415', '300671', '601128', '300111', '002595', '603689', '002644', '002271', '600998', '600133', '300211', '600831', '300232', '300484', '600428', '603811', '002308', '002283', '600518', '603041', '002623', '002789', '600166', '000301', '600230', '300282', '002328', '300565', '600655', '300707', '002166', '002849', '300332', '300219', '603871', '601965', '601880',
    '002505', '002757', '600839', '300187', '300607', '300597', '300514', '300537', '601058', '002156', '603188', '600846', '600811', '600828', '300463', '000595', '300638', '300336', '601777', '600505', '603896', '002697', '300381', '001965', '002261', '002255', '002572', '300512', '600973', '002916', '002800', '000919', '300147', '000651', '300018', '603203', '000591', '000622', '300653', '300052', '600108', '002481', '002340', '600101', '300568', '002728', '600382', '300113', '002574', '600686', '601198', '002885', '600444', '601208', '002690', '300154', '002743', '002154', '603586', '300040', '002823', '600139', '300629', '300073', '601069', '300610', '600288', '300194', '600012', '600250', '002852', '603338', '603360', '600361', '000571', '300179', '300223', '002211', '603283', '601212', '600052', '000589', '600775', '300453', '002087', '603626', '600338', '600073', '601607', '300679', '002432', '000722', '002675', '000655', '603707', '000617', '002326', '300055', '002218',
    '002642', '600495', '002119', '600857', '600301', '002548', '603868', '300242', '002332', '000425', '600319', '300715', '000835', '603227', '300222', '002855', '002529', '002220', '002364', '300088', '300369', '300509', '300342', '002424', '601952', '000608', '600749', '000068', '000902', '600891', '600475', '002755', '603900', '300076', '002785', '000420', '002579', '300161', '600592', '600598', '603990', '600155', '000861', '600703', '300057', '000014', '600467', '000659', '600750', '600118', '600128', '002513', '002431', '002130', '002242', '002194', '300492', '000656', '601588', '600835', '002420', '002818', '600115', '002774', '300123', '300690', '002489', '002900', '603928', '000928', '002609', '002266', '300200', '600057', '002305', '002207', '603330', '300577', '000971', '300177', '300633', '600435', '002392', '300723', '000560', '002913', '002190', '603669', '002380', '002733', '300407', '300644', '000677', '002023', '002425', '600805', '600908', '002272', '600251',
    '603903', '002306', '000978', '600917', '002886', '002275', '601999', '603633', '603683', '603505', '002465', '600869', '603797', '300349', '601838', '600100', '000678', '002907', '002112', '000859', '002223', '000584', '002236', '300133', '002925', '000821', '603298', '600834', '603016', '600854', '000421', '300344', '002338', '002334', '002157', '300138', '002078', '000518', '300481', '300469', '600978', '300017', '002875', '600415', '000637', '002689', '300581', '002176', '603993', '002022', '603099', '603030', '300692', '002270', '300599', '002446', '000536', '300253', '300661', '002651', '600616', '600373', '600162', '603698', '000705', '000039', '000548', '002253', '603958', '002325', '002667', '002758', '000716', '002329', '600298', '002688', '600731', '002348', '603319', '300389', '300720', '002777', '600498', '002780', '600573', '300265', '000712', '600317', '600077', '002819', '000800', '300144', '600511', '603825', '002641', '300698', '600071', '300013', '002089',
    '000011', '000620', '300296', '000599', '002598', '600704', '601200', '000551', '600981', '600075', '000981', '603218', '002399', '002751', '600679', '300506', '600408', '300190', '300536', '603929', '300230', '300053', '600337', '603305', '002456', '002017', '002231', '603300', '000543', '000811', '300421', '002504', '002827', '002401', '300024', '603017', '600633', '600681', '603186', '300436', '300525', '600778', '603679', '002593', '600796', '002748', '300489', '600558', '600310', '603323', '000852', '603313', '600610', '300370', '300605', '300418', '000721', '002448', '002772', '600640', '000158', '600477', '600336', '300535', '600644', '600851', '600258', '002133', '002026', '000040', '600272', '300448', '002342', '600120', '603999', '002766', '300197', '002169', '002375', '002138', '002269', '300510', '300346', '600774', '603336', '600589', '300434', '300155', '600867', '300203', '603819', '300079', '603078', '600056', '600617', '603838', '600671', '000733', '002637',
    '300528', '002106', '000582', '300414', '000681', '600068', '300124', '601333', '300394', '603101', '002215', '002389', '300267', '603266', '000702', '000058', '603615', '600513', '600677', '002400', '300303', '002153', '600066', '000030', '002430', '300305', '600890', '300027', '600006', '600385', '601718', '600624', '300110', '000639', '603320', '600371', '300352', '002555', '300261', '002355', '000061', '002636', '000544', '002645', '002314', '300143', '000889', '002880', '000908', '300205', '600198', '002062', '300502', '002676', '300176', '000915', '600506', '601558', '603986', '600018', '300499', '601798', '002573', '002568', '002158', '000078', '603969', '300093', '000905', '002807', '300009', '600490', '002344', '002300', '000048', '300115', '002232', '603716', '600676', '300318', '300212', '002282', '600178', '300263', '600737', '600149', '600620', '002081', '000692', '000988', '600275', '000801', '000018', '600281', '002131', '000701', '000882', '600097', '300592',
    '600421', '002251', '600173', '300025', '002790', '002295', '002181', '002135', '002605', '002115', '002238', '300292', '600841', '603258', '600868', '603366', '600469', '300701', '002132', '603025', '600458', '002313', '300045', '600081', '300639', '300562', '002152', '002299', '300518', '300157', '600193', '002361', '002787', '300323', '603067', '600761', '600612', '002709', '600879', '600391', '002590', '600200', '300095', '300572', '002354', '000881', '002406', '000572', '601579', '603306', '600482', '600353', '002470', '000779', '601222', '000753', '300480', '002640', '600352', '603058', '600730', '600717', '002360', '000088', '603127', '300302', '600232', '300207', '600578', '002556', '000570', '603111', '002316', '601228', '600237', '002477', '300362', '002543', '600107', '002510', '000711', '002046', '000759', '300505', '600222', '603611', '603828', '002274', '600893', '002035', '002177', '002335', '300543', '603385', '000026', '300493', '603588', '300171', '000920',
    '002140', '300046', '300131', '600476', '603239', '300340', '002458', '600862', '300284', '603936', '000669', '300531', '000738', '000593', '002659', '300215', '002615', '300268', '002006', '603088', '000901', '300503', '002350', '000042', '002494', '600755', '002808', '300319', '603559', '600105', '002322', '002713', '000756', '002700', '000862', '603158', '002222', '000409', '601567', '300150', '600261', '002838', '300307', '600456', '002214', '600256', '300416', '600358', '603328', '300102', '300084', '603656', '002052', '300244', '600855', '600343', '002610', '000982', '600459', '300443', '603496', '002551', '601599', '002588', '002824', '300546', '600817', '000662', '002553', '000521', '300486', '300428', '600836', '300162', '300725', '300612', '601137', '600590', '601958', '600530', '603113', '300538', '300005', '300016', '000017', '300002', '300299', '300722', '600896', '300326', '002105', '300540', '002594', '600593', '600372', '002576', '002831', '002670', '300471',
    '002526', '603806', '300092', '002767', '002546', '601000', '300105', '600070', '600480', '300445', '002862', '300334', '002277', '603813', '300235', '300521', '300139', '300579', '002011', '300227', '600195', '002487', '000997', '300192', '002750', '002292', '600153', '603159', '002246', '300249', '600630', '600692', '300175', '300404', '300589', '000619', '300440', '000558', '000838', '002265', '300121', '002708', '002832', '300338', '600662', '002217', '603399', '603800', '000819', '000676', '600898', '300114', '002079', '600532', '300427', '002436', '300417', '600163', '603855', '001896', '603011', '300573', '600234', '603168', '300474', '600673', '601038', '300571', '002123', '601008', '300074', '603678', '002351', '300567', '300256', '002323', '300628', '000567', '600651', '300442', '002616', '600537', '600152', '300451', '600238', '002776', '300315', '601890', '002224', '603006', '002846', '300036', '600029', '002471', '002041', '002877', '300310', '300250', '002714',
    '300012', '300603', '300412', '300449', '002241', '000597', '603456', '600545', '300600', '002897', '002779', '600768', '002358', '002712', '000032', '002076', '002759', '002624', '300385', '002649', '300101', '603926', '300452', '300378', '300549', '300673', '600770', '300391', '300050', '600354', '002583', '600055', '600619', '002045', '603861', '300021', '000628', '002173', '600791', '600072', '600626', '300516', '000565', '300030', '600845', '002303', '002031', '600939', '002763', '603039', '600520', '603528', '600838', '600696', '002030', '000785', '300208', '000790', '300473', '002528', '002124', '002444', '000829', '603031', '300675', '300384', '603015', '002781', '600810', '002473', '000050', '600292', '600527', '300366', '300719', '002339', '300357', '300461', '300254', '002768', '000710', '603803', '300494', '601858', '300043', '300373', '600776', '002693', '002296', '600653', '300458', '002558', '002226', '600125', '600654', '300447', '300140', '600218', '000938',
    '300329', '600667', '600446', '600818', '603602', '600718', '002599', '300354', '300042', '002783', '603042', '300397', '000609', '002506', '002025', '300402', '002396', '002235', '000836', '300313', '300331', '601086', '600267', '002762', '300388', '300350', '000679', '600797', '300406', '600360', '600975', '000021', '002291', '603578', '603387', '600650', '000839', '000502', '002172', '000520', '002729', '603010', '002786', '300142', '002297', '002829', '002362', '603118', '000665', '603557', '600420', '300359', '600565', '603023', '000153', '300276', '000980', '300539', '300297', '000010', '600186', '300287', '000045', '002367', '300419', '300184', '300552', '603126', '000707', '300152', '603978', '603789', '300515', '002503', '601326', '600088', '002517', '603022', '600416', '300063', '002381', '002070', '300405', '002104', '603808', '600584', '300456', '300532', '300098', '600889', '300487', '002331', '002429', '603987', '300167', '300148', '002835', '002036', '300109',
    '603416', '002822', '600765', '002118', '300034', '000507', '002696', '300343', '002418', '002826', '300339', '002195', '600603', '002188', '600613', '300588', '300609', '300288', '002695', '603895', '300708', '000823', '002185', '000887', '002892', '603877', '002810', '600745', '603933', '002492', '600099', '000062', '002463', '002544', '300007', '600698', '002539', '300413', '600316', '601800', '000723', '300627', '600602', '002467', '603005', '300306', '000627', '000700', '000782', '603817', '300696', '600689', '600576', '300304', '600137', '300316', '300022', '600074', '300631', '002279', '002698', '000815', '002247', '002093', '002474', '002058', '002009', '300293', '600359', '002264', '002760', '300585', '600038', '603628', '300247', '002180', '002273', '300019', '300460', '600302', '300476', '600113', '300047', '300234', '002830', '002419', '601231', '603883', '300693', '603970', '300264', '002570', '300604', '600526', '300277', '002684', '000066', '300433', '002702',
    '002836', '300345', '002677', '300446', '002405', '300291', '002581', '300023', '300364', '002618', '600570', '002065', '300468', '300245', '300606', '300601', '000996', '300011', '600202', '300324', '002343', '300426', '000070', '300251', '300333', '002040', '300210', '300608', '300598', '300259', '603703', '300275', '002200', '600171', '300097', '600119', '300044', '600410', '603106', '000868', '002839', '002439', '002735', '000893', '002368', '002416', '000948', '002315', '300465', '600622', '600990', '600289', '002569', '300555', '300061', '300386', '300380', '603128', '300031', '002638', '603286', '300209', '600523', '300676', '600732', '300399', '300226', '300295', '002049', '603108', '600571', '002843', '603096', '601100', '300691', '002771', '002795', '002869', '300566', '000670', '603363', '600850', '601116', '600460', '300213', '600313', '002707', '600265', '300630', '002129', '300495', '600967', '300348', '300368', '300248', '002486', '603232', '300738', '600562',
    '600760', '600278', '300551', '300201', '300241', '300467', '603007', '002793', '603177', '300496', '603355', '002054', '002896', '300347', '000760', '300541', '600609', '002013', '603138', '300706', '600247', '300557', '603901', '603083', '000020', '300377', '002376', '300246', '600721', '002891', '000995', '000519', '600716', '002476', '300252', '300527', '000957', '603189', '300077', '300730', '300311', '002722', '000025', '300028', '600756', '603918', '600533', '603938', '000004', '002657', '000561', '300271', '603499', '600560', '300188', '600211', '300182', '000768', '300112', '002856', '000006', '300681', '300085', '603988', '002606', '002388', '600822', '002069', '002371', '603648', '600525', '300183', '300170', '002063', '300520', '002175', '603103', '600643', '300466', '600579', '300078', '000806', '000638', '600379', '000530', '300430', '600517', '300122', '300300', '000977', '000816', '603516', '603056', '300687', '300584', '002668', '601366', '600213', '300236',
    '300367', '000007', '600463', '002095', '300560', '300556', '603329', '600536', '300216', '002560', '603356', '300298', '603019', '600789', '300431', '300561', '300677', '300066', '300166', '600093', '300663', '300685', '002879', '601360', '002912', '300684', '300542', '300314', '600588', '601700', '600634', '300504', '002931', '000950', '000629', '000511', '603214', '600929', '600806', '600432'
]

# id = ['000825', '002110', '002077', '600507', '600809', '000825', '600559', '600010', '600516', '002248', '600887']

def isMaRise(info):     #002004
    # 当天ma20大于前一天ma20， 说明ma处于回升状态
    if np.isnan(info.ma20[0].item()):        # 20日均线结果为 NaN
        return False

    if info.ma20[0] >= info.ma20[1]:
        return True
    else:
        return False

    # return  True

def priceBreakMA20(info):
    """
    当天价格图破20日均线
    :param info:
    :return:
    """
    if isMaRise(info):
        ma20 = info.ma20[0]
        close = info.close[0]
        open = info.open[0]

        if close > ma20 and open < ma20:
            return True
        else:
            return False
    pass

def priceLessThanMA20(info):
    if isMaRise(info):
        ma20 = info.ma20[0]
        close = info.close[0]
        if ma20 > close and (ma20 - close)/close < 0.1:
            return True
        else:
            return False


def searchStock():
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f_less = open('less'+t+'.txt', 'w')
    f_break = open('break'+t+'.txt', 'w')
    cons = ts.get_apis()
    for num in range(0, len(id)):
        print('当前读取股票代码 %s, 已经检索 %d' % (id[num], num))
        try:
            info = ts.bar(id[num], conn=cons, start_date='2018-01-13', end_date='2018-03-14', ma=[5, 10, 20], adj='qfq')
        except:
            pass
        else:
            if priceBreakMA20(info):
                f_break.write(info.code[0])
                print('-----------------%s 穿过20日均线' % info.code[0])
            if priceLessThanMA20(info):
                f_less.write(info.code[0] + '\n')
                print('!!!!!!!!!!!!!!!!!%s 小于20日均线' % info.code[0])

    f_less.close()
    f_break.close()
    ts.close_apis(cons)


if __name__ == '__main__':
    searchStock()

