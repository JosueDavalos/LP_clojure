
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DEF HASHMAP SORTEDMAP MAP VECTOR CONJUNTO STR LOOP WHILE DO WHEN PRINTLN PRINT RECUR DEFN FIRST LISTA NTH IF TRUE FALSE READ LINE NOT AND OR CONS GET CONJ KEYS ENTERO FLOTANTE STRING PAR_DER PAR_IZQ COR_DER COR_IZQ SUM REST PRODUCT DIVISION EQUAL NOT_EQUAL GREATER_THAN LESS_THAN GREATER_THAN_EQUAL LESS_THAN_EQUAL COM_SIM NOMBRE HASH LLAV_IZQ LLAV_DER COMAsentencia_compuesta : algoritmo\n                           | algoritmo sentencia_compuesta\n    algoritmo : variable\n                 | expresion\n                 | imprimir\n                 | estructurasControl\n                 | funcion\n                 | metodo_lista\n                 | metodo_conjunto\n                 | metodo_vector\n                 | metodo_mapas\n    funcion : PAR_IZQ DEFN NOMBRE argumentos sentencia_compuesta PAR_DERargumentos :  COR_IZQ argumento COR_DER\n                  | COR_IZQ COR_DER\n    argumento : NOMBRE\n                 | NOMBRE argumento\n    metodo_lista : PAR_IZQ FIRST NOMBRE PAR_DER\n                    | PAR_IZQ FIRST estructura_lista PAR_DERmetodo_lista : PAR_IZQ NTH NOMBRE NOMBRE PAR_DER\n                    | PAR_IZQ NTH NOMBRE ENTERO PAR_DER\n                    | PAR_IZQ NTH estructura_lista ENTERO PAR_DER\n                    | PAR_IZQ NTH estructura_lista NOMBRE PAR_DERmetodo_lista : PAR_IZQ CONS valor NOMBRE PAR_DER\n                    | PAR_IZQ CONS valor estructura_lista PAR_DERmetodo_conjunto : PAR_IZQ GET estructura_conjunto NOMBRE PAR_DER\n                       | PAR_IZQ GET estructura_conjunto ENTERO PAR_DER\n    metodo_conjunto : PAR_IZQ CONJ estructura_conjunto valor PAR_DERmetodo_vector : PAR_IZQ GET estructura_vector NOMBRE PAR_DER\n                     | PAR_IZQ GET estructura_vector ENTERO PAR_DER\n    metodo_vector : PAR_IZQ CONJ estructura_vector valor PAR_DERmetodo_mapas : PAR_IZQ GET estructura_mapa STRING PAR_DER\n                    | PAR_IZQ GET estructura_mapa NOMBRE PAR_DER\n                    | PAR_IZQ GET NOMBRE NOMBRE PAR_DER\n                    | PAR_IZQ GET NOMBRE STRING PAR_DER\n    metodo_mapas : PAR_IZQ KEYS estructura_mapa PAR_DER\n                    | PAR_IZQ KEYS NOMBRE PAR_DERvariable : PAR_IZQ DEF NOMBRE expresion PAR_DERexpresion : valor\n                 | estructura\n                 | expresionAritmetica\n                 | comparacion\n                 | comparacionLogica\n                 | input\n    estructura : estructura_mapa\n                  | estructura_lista\n                  | estructura_conjunto\n                  | estructura_vector estructurasControl : if\n                           | while\n                           | loop\n    loop : PAR_IZQ LOOP COR_IZQ compuesto COR_DER when PAR_DER\n    when : PAR_IZQ WHEN comparacion algoritmo recur PAR_DER\n    recur : PAR_IZQ RECUR expresionAritmetica PAR_DER\n    while : PAR_IZQ WHILE comparacion PAR_IZQ DO sentencia_compuesta PAR_DER PAR_DER\n    if : PAR_IZQ IF expresionBooleana sentencia_compuesta PAR_DERexpresionBooleana : FALSE\n                         | TRUE\n                         | comparacionLogica\n                         | comparacion\n    input : PAR_IZQ READ REST LINE PAR_DERimprimir : PAR_IZQ opcionesImprimir expresion PAR_DER\n    comparacionLogica :  PAR_IZQ operadorLogico valor valor PAR_DER\n                         | PAR_IZQ NOT valor PAR_DER\n    comparacion : PAR_IZQ operadorComparacion valor valor PAR_DERexpresionAritmetica : PAR_IZQ operadorMat numberoSerie PAR_DER\n    numberoSerie : numero\n                    | NOMBRE\n                    | expresionAritmetica\n                    | numero numberoSerie\n                    | NOMBRE numberoSerie\n                    | expresionAritmetica numberoSerie\n    estructura_lista : PAR_IZQ LISTA PAR_IZQ compuesto PAR_DER PAR_DER\n                        | COM_SIM PAR_IZQ compuesto PAR_DER\n                        | PAR_IZQ LISTA compuesto PAR_DER\n    estructura_conjunto : PAR_IZQ CONJUNTO COM_SIM PAR_IZQ compuesto PAR_DER PAR_DER\n                           | HASH LLAV_IZQ compuesto LLAV_DER\n    estructura_vector : PAR_IZQ VECTOR compuesto PAR_DER\n                         | COR_IZQ compuesto COR_DER\n    estructura_mapa : LLAV_IZQ parclaves LLAV_DER\n                       | PAR_IZQ mapas parclaves PAR_DER\n    mapas : SORTEDMAP REST MAP\n             | HASHMAP REST MAP\n    compuesto : valor\n                 | valor compuesto\n    parclaves : STRING STRING\n                 | STRING STRING COMA parclaves\n                 | STRING STRING parclaves\n    valor : numero\n             | NOMBRE\n             | booleano\n             | cadena\n    cadena : STRING\n              | PAR_IZQ STR STRING STRING PAR_DER\n    booleano : TRUE\n                | FALSE\n    numero : ENTERO\n              | FLOTANTE\n    operadorMat : SUM\n                   | REST\n                   | PRODUCT\n                   | DIVISION\n    operadorComparacion : EQUAL\n                           | NOT_EQUAL\n                           | GREATER_THAN\n                           | LESS_THAN\n                           | GREATER_THAN_EQUAL\n                           | LESS_THAN_EQUAL\n    operadorLogico : AND\n                      | OR\n    opcionesImprimir : PRINT\n                        | PRINTLN\n    '
    
_lr_action_items = {'PAR_IZQ':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,41,43,44,45,46,47,48,49,50,51,52,54,55,56,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,83,84,85,94,101,102,108,109,110,111,112,116,117,118,119,120,122,123,126,128,132,134,139,140,142,143,160,161,162,168,174,176,177,178,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,216,217,222,225,226,227,228,229,230,233,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,80,-97,-94,-95,83,86,89,89,80,95,100,103,106,80,80,80,-99,115,121,126,80,-110,-111,-98,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,80,80,80,86,89,80,80,106,106,106,80,80,12,-56,-57,-58,-59,171,80,80,177,-78,-79,-61,12,-17,-18,-35,-36,-65,-63,-80,-74,80,-77,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,12,220,-93,-12,-13,-72,121,-51,-75,-54,12,231,106,]),'NOMBRE':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,40,41,42,43,44,45,46,48,49,50,51,52,54,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,83,84,85,92,93,94,96,97,98,99,101,102,108,109,110,111,112,116,117,118,119,120,123,126,132,134,139,140,141,142,143,160,161,162,168,174,176,177,178,183,184,185,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,13,-97,-94,-95,85,13,88,90,92,13,97,105,109,13,13,13,-99,13,13,-110,-111,-98,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,13,13,13,13,144,147,148,150,152,154,157,13,13,109,109,109,13,13,13,-56,-57,-58,-59,13,13,-78,-79,-61,13,189,-17,-18,-35,-36,-65,-63,-80,-74,13,-77,-73,-76,-37,-14,189,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,13,-93,-12,-13,-72,-51,-75,-54,13,]),'ENTERO':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,41,45,49,50,51,52,54,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,83,84,85,92,93,96,98,101,102,108,109,110,111,112,116,117,118,119,120,123,126,132,134,139,140,142,143,160,161,162,168,174,176,177,178,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,24,-97,-94,-95,24,24,24,24,24,24,-99,24,24,-110,-111,-98,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,24,24,24,24,145,146,151,155,24,24,24,24,24,24,24,24,-56,-57,-58,-59,24,24,-78,-79,-61,24,-17,-18,-35,-36,-65,-63,-80,-74,24,-77,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,24,-93,-12,-13,-72,-51,-75,-54,24,]),'FLOTANTE':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,41,45,49,50,51,52,54,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,83,84,85,101,102,108,109,110,111,112,116,117,118,119,120,123,126,132,134,139,140,142,143,160,161,162,168,174,176,177,178,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[33,33,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,33,-97,-94,-95,33,33,33,33,33,33,-99,33,33,-110,-111,-98,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,33,33,33,33,33,33,33,33,33,33,33,33,-56,-57,-58,-59,33,33,-78,-79,-61,33,-17,-18,-35,-36,-65,-63,-80,-74,33,-77,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,33,-93,-12,-13,-72,-51,-75,-54,33,]),'TRUE':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,41,45,50,51,52,55,60,62,63,64,68,69,70,71,72,73,74,75,79,83,84,85,101,102,111,112,116,117,118,119,120,123,126,132,134,139,140,142,143,160,161,162,168,174,176,177,178,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[34,34,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,34,-97,-94,-95,34,34,34,34,34,118,34,34,-110,-111,-102,-103,-104,-105,-106,-107,-108,-109,34,34,34,34,34,34,34,34,34,-56,-57,-58,-59,34,34,-78,-79,-61,34,-17,-18,-35,-36,-65,-63,-80,-74,34,-77,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,34,-93,-12,-13,-72,-51,-75,-54,34,]),'FALSE':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,41,45,50,51,52,55,60,62,63,64,68,69,70,71,72,73,74,75,79,83,84,85,101,102,111,112,116,117,118,119,120,123,126,132,134,139,140,142,143,160,161,162,168,174,176,177,178,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[35,35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,35,-97,-94,-95,35,35,35,35,35,117,35,35,-110,-111,-102,-103,-104,-105,-106,-107,-108,-109,35,35,35,35,35,35,35,35,35,-56,-57,-58,-59,35,35,-78,-79,-61,35,-17,-18,-35,-36,-65,-63,-80,-74,35,-77,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,35,-93,-12,-13,-72,-51,-75,-54,35,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,41,45,50,51,52,58,59,60,62,63,64,68,69,70,71,72,73,74,75,79,82,83,84,85,97,99,101,102,111,112,116,117,118,119,120,123,124,126,132,134,135,139,140,142,143,160,161,162,168,174,176,177,178,179,180,181,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,28,-97,-94,-95,82,28,28,28,28,28,124,82,28,28,-110,-111,-102,-103,-104,-105,-106,-107,-108,-109,28,135,28,28,28,153,156,28,28,28,28,28,-56,-57,-58,-59,28,173,28,-78,-79,82,-61,28,-17,-18,-35,-36,-65,-63,-80,-74,28,-77,-81,-82,82,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,28,-93,-12,-13,-72,-51,-75,-54,28,]),'LLAV_IZQ':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,38,41,46,48,63,64,85,116,117,118,119,120,132,134,139,140,142,143,160,161,162,168,174,176,178,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[36,36,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,-97,-94,-95,84,36,36,36,-110,-111,36,36,-56,-57,-58,-59,-78,-79,-61,36,-17,-18,-35,-36,-65,-63,-80,-74,-77,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,36,-93,-12,-13,-72,-51,-75,-54,36,]),'COM_SIM':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,41,43,44,61,63,64,85,94,116,117,118,119,120,132,134,139,140,142,143,160,161,162,168,174,176,178,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[37,37,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,-97,-94,-95,37,37,37,128,-110,-111,37,37,37,-56,-57,-58,-59,-78,-79,-61,37,-17,-18,-35,-36,-65,-63,-80,-74,-77,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,37,-93,-12,-13,-72,-51,-75,-54,37,]),'HASH':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,41,46,47,63,64,85,116,117,118,119,120,132,134,139,140,142,143,160,161,162,168,174,176,178,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[38,38,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,-97,-94,-95,38,38,38,-110,-111,38,38,-56,-57,-58,-59,-78,-79,-61,38,-17,-18,-35,-36,-65,-63,-80,-74,-77,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,38,-93,-12,-13,-72,-51,-75,-54,38,]),'COR_IZQ':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,41,46,47,57,63,64,85,88,116,117,118,119,120,132,134,139,140,142,143,160,161,162,168,174,176,178,183,184,185,188,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,212,216,217,222,226,227,228,229,],[32,32,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,-97,-94,-95,32,32,32,123,-110,-111,32,141,32,-56,-57,-58,-59,-78,-79,-61,32,-17,-18,-35,-36,-65,-63,-80,-74,-77,-73,-76,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,32,-93,-12,-13,-72,-51,-75,-54,32,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,39,132,134,139,142,143,160,161,162,168,174,176,178,183,184,185,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,212,216,222,226,227,228,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,-97,-94,-95,-2,-78,-79,-61,-17,-18,-35,-36,-65,-63,-80,-74,-77,-73,-76,-37,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,-93,-12,-72,-51,-75,-54,]),'PAR_DER':([2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,39,79,87,90,91,104,105,107,108,109,110,113,125,127,129,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,173,174,175,176,178,182,183,184,185,186,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,212,213,214,215,216,219,221,222,223,224,226,227,228,232,234,235,236,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-89,-38,-39,-40,-41,-42,-43,-48,-49,-50,-45,-96,-46,-47,-44,-92,-88,-90,-91,-97,-94,-95,-2,-83,139,142,143,160,161,162,-66,-67,-68,168,174,176,178,-78,-84,-79,-85,183,185,-61,-17,-18,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,-35,-36,-65,-69,-70,-71,206,207,-63,208,209,212,-80,213,-74,-77,-87,-73,-76,-37,216,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-64,-62,-60,-55,-93,222,223,-86,-12,224,226,-72,227,228,-51,-75,-54,234,-52,236,-53,]),'DEF':([12,],[40,]),'DEFN':([12,],[42,]),'FIRST':([12,],[43,]),'NTH':([12,],[44,]),'CONS':([12,],[45,]),'GET':([12,],[46,]),'CONJ':([12,],[47,]),'KEYS':([12,],[48,]),'NOT':([12,86,115,],[52,52,52,]),'READ':([12,86,],[53,53,]),'IF':([12,],[55,]),'WHILE':([12,],[56,]),'LOOP':([12,],[57,]),'STR':([12,80,86,126,],[58,58,58,58,]),'LISTA':([12,86,89,],[60,60,60,]),'CONJUNTO':([12,86,95,100,],[61,61,61,61,]),'VECTOR':([12,86,95,100,],[62,62,62,62,]),'PRINT':([12,],[63,]),'PRINTLN':([12,],[64,]),'SUM':([12,86,106,],[65,65,65,]),'REST':([12,53,76,77,86,106,],[54,114,130,131,54,54,]),'PRODUCT':([12,86,106,],[66,66,66,]),'DIVISION':([12,86,106,],[67,67,67,]),'EQUAL':([12,86,115,121,],[68,68,68,68,]),'NOT_EQUAL':([12,86,115,121,],[69,69,69,69,]),'GREATER_THAN':([12,86,115,121,],[70,70,70,70,]),'LESS_THAN':([12,86,115,121,],[71,71,71,71,]),'GREATER_THAN_EQUAL':([12,86,115,121,],[72,72,72,72,]),'LESS_THAN_EQUAL':([12,86,115,121,],[73,73,73,73,]),'AND':([12,86,115,],[74,74,74,]),'OR':([12,86,115,],[75,75,75,]),'SORTEDMAP':([12,86,95,103,],[76,76,76,76,]),'HASHMAP':([12,86,95,103,],[77,77,77,77,]),'COR_DER':([13,24,28,29,30,31,33,34,35,78,79,133,141,172,187,189,212,218,],[-89,-96,-92,-88,-90,-91,-97,-94,-95,132,-83,-84,188,211,217,-15,-93,-16,]),'LLAV_DER':([13,24,28,29,30,31,33,34,35,79,81,133,135,137,182,212,215,],[-89,-96,-92,-88,-90,-91,-97,-94,-95,-83,134,-84,-85,184,-87,-93,-86,]),'LINE':([114,],[169,]),'MAP':([130,131,],[179,180,]),'COMA':([135,],[181,]),'DO':([171,],[210,]),'WHEN':([220,],[225,]),'RECUR':([231,],[233,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia_compuesta':([0,2,116,140,210,],[1,39,170,186,219,]),'algoritmo':([0,2,116,140,210,229,],[2,2,2,2,2,230,]),'variable':([0,2,116,140,210,229,],[3,3,3,3,3,3,]),'expresion':([0,2,41,85,116,140,210,229,],[4,4,87,138,4,4,4,4,]),'imprimir':([0,2,116,140,210,229,],[5,5,5,5,5,5,]),'estructurasControl':([0,2,116,140,210,229,],[6,6,6,6,6,6,]),'funcion':([0,2,116,140,210,229,],[7,7,7,7,7,7,]),'metodo_lista':([0,2,116,140,210,229,],[8,8,8,8,8,8,]),'metodo_conjunto':([0,2,116,140,210,229,],[9,9,9,9,9,9,]),'metodo_vector':([0,2,116,140,210,229,],[10,10,10,10,10,10,]),'metodo_mapas':([0,2,116,140,210,229,],[11,11,11,11,11,11,]),'valor':([0,2,32,41,45,50,51,52,60,62,79,83,84,85,101,102,111,112,116,123,126,140,177,210,229,],[14,14,79,14,94,111,112,113,79,79,79,79,79,14,158,159,166,167,14,79,79,14,79,14,14,]),'estructura':([0,2,41,85,116,140,210,229,],[15,15,15,15,15,15,15,15,]),'expresionAritmetica':([0,2,41,49,85,108,109,110,116,140,210,229,233,],[16,16,16,110,16,110,110,110,16,16,16,16,235,]),'comparacion':([0,2,41,55,56,85,116,140,210,225,229,],[17,17,17,120,122,17,17,17,17,229,17,]),'comparacionLogica':([0,2,41,55,85,116,140,210,229,],[18,18,18,119,18,18,18,18,18,]),'input':([0,2,41,85,116,140,210,229,],[19,19,19,19,19,19,19,19,]),'if':([0,2,116,140,210,229,],[20,20,20,20,20,20,]),'while':([0,2,116,140,210,229,],[21,21,21,21,21,21,]),'loop':([0,2,116,140,210,229,],[22,22,22,22,22,22,]),'estructura_lista':([0,2,41,43,44,85,94,116,140,210,229,],[23,23,23,91,93,23,149,23,23,23,23,]),'estructura_conjunto':([0,2,41,46,47,85,116,140,210,229,],[25,25,25,96,101,25,25,25,25,25,]),'estructura_vector':([0,2,41,46,47,85,116,140,210,229,],[26,26,26,98,102,26,26,26,26,26,]),'estructura_mapa':([0,2,41,46,48,85,116,140,210,229,],[27,27,27,99,104,27,27,27,27,27,]),'numero':([0,2,32,41,45,49,50,51,52,60,62,79,83,84,85,101,102,108,109,110,111,112,116,123,126,140,177,210,229,],[29,29,29,29,29,108,29,29,29,29,29,29,29,29,29,29,29,108,108,108,29,29,29,29,29,29,29,29,29,]),'booleano':([0,2,32,41,45,50,51,52,60,62,79,83,84,85,101,102,111,112,116,123,126,140,177,210,229,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'cadena':([0,2,32,41,45,50,51,52,60,62,79,83,84,85,101,102,111,112,116,123,126,140,177,210,229,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'opcionesImprimir':([12,],[41,]),'operadorMat':([12,86,106,],[49,49,49,]),'operadorComparacion':([12,86,115,121,],[50,50,50,50,]),'operadorLogico':([12,86,115,],[51,51,51,]),'mapas':([12,86,95,103,],[59,59,59,59,]),'compuesto':([32,60,62,79,83,84,123,126,177,],[78,127,129,133,136,137,172,175,214,]),'parclaves':([36,59,135,181,],[81,125,182,215,]),'numberoSerie':([49,108,109,110,],[107,163,164,165,]),'expresionBooleana':([55,],[116,]),'argumentos':([88,],[140,]),'argumento':([141,189,],[187,218,]),'when':([211,],[221,]),'recur':([230,],[232,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencia_compuesta","S'",1,None,None,None),
  ('sentencia_compuesta -> algoritmo','sentencia_compuesta',1,'p_sentencia_compuesta','sintactico.py',6),
  ('sentencia_compuesta -> algoritmo sentencia_compuesta','sentencia_compuesta',2,'p_sentencia_compuesta','sintactico.py',7),
  ('algoritmo -> variable','algoritmo',1,'p_algoritmo','sintactico.py',11),
  ('algoritmo -> expresion','algoritmo',1,'p_algoritmo','sintactico.py',12),
  ('algoritmo -> imprimir','algoritmo',1,'p_algoritmo','sintactico.py',13),
  ('algoritmo -> estructurasControl','algoritmo',1,'p_algoritmo','sintactico.py',14),
  ('algoritmo -> funcion','algoritmo',1,'p_algoritmo','sintactico.py',15),
  ('algoritmo -> metodo_lista','algoritmo',1,'p_algoritmo','sintactico.py',16),
  ('algoritmo -> metodo_conjunto','algoritmo',1,'p_algoritmo','sintactico.py',17),
  ('algoritmo -> metodo_vector','algoritmo',1,'p_algoritmo','sintactico.py',18),
  ('algoritmo -> metodo_mapas','algoritmo',1,'p_algoritmo','sintactico.py',19),
  ('funcion -> PAR_IZQ DEFN NOMBRE argumentos sentencia_compuesta PAR_DER','funcion',6,'p_funcion','sintactico.py',24),
  ('argumentos -> COR_IZQ argumento COR_DER','argumentos',3,'p_argumentos','sintactico.py',27),
  ('argumentos -> COR_IZQ COR_DER','argumentos',2,'p_argumentos','sintactico.py',28),
  ('argumento -> NOMBRE','argumento',1,'p_argumento','sintactico.py',32),
  ('argumento -> NOMBRE argumento','argumento',2,'p_argumento','sintactico.py',33),
  ('metodo_lista -> PAR_IZQ FIRST NOMBRE PAR_DER','metodo_lista',4,'p_metodo_lista_first','sintactico.py',38),
  ('metodo_lista -> PAR_IZQ FIRST estructura_lista PAR_DER','metodo_lista',4,'p_metodo_lista_first','sintactico.py',39),
  ('metodo_lista -> PAR_IZQ NTH NOMBRE NOMBRE PAR_DER','metodo_lista',5,'p_metodo_lista_nth','sintactico.py',43),
  ('metodo_lista -> PAR_IZQ NTH NOMBRE ENTERO PAR_DER','metodo_lista',5,'p_metodo_lista_nth','sintactico.py',44),
  ('metodo_lista -> PAR_IZQ NTH estructura_lista ENTERO PAR_DER','metodo_lista',5,'p_metodo_lista_nth','sintactico.py',45),
  ('metodo_lista -> PAR_IZQ NTH estructura_lista NOMBRE PAR_DER','metodo_lista',5,'p_metodo_lista_nth','sintactico.py',46),
  ('metodo_lista -> PAR_IZQ CONS valor NOMBRE PAR_DER','metodo_lista',5,'p_metodo_lista_cons','sintactico.py',50),
  ('metodo_lista -> PAR_IZQ CONS valor estructura_lista PAR_DER','metodo_lista',5,'p_metodo_lista_cons','sintactico.py',51),
  ('metodo_conjunto -> PAR_IZQ GET estructura_conjunto NOMBRE PAR_DER','metodo_conjunto',5,'p_metodo_conjunto_get','sintactico.py',56),
  ('metodo_conjunto -> PAR_IZQ GET estructura_conjunto ENTERO PAR_DER','metodo_conjunto',5,'p_metodo_conjunto_get','sintactico.py',57),
  ('metodo_conjunto -> PAR_IZQ CONJ estructura_conjunto valor PAR_DER','metodo_conjunto',5,'p_metodo_conjunto_conj','sintactico.py',62),
  ('metodo_vector -> PAR_IZQ GET estructura_vector NOMBRE PAR_DER','metodo_vector',5,'p_metodo_vector_get','sintactico.py',67),
  ('metodo_vector -> PAR_IZQ GET estructura_vector ENTERO PAR_DER','metodo_vector',5,'p_metodo_vector_get','sintactico.py',68),
  ('metodo_vector -> PAR_IZQ CONJ estructura_vector valor PAR_DER','metodo_vector',5,'p_metodo_vector_conj','sintactico.py',73),
  ('metodo_mapas -> PAR_IZQ GET estructura_mapa STRING PAR_DER','metodo_mapas',5,'p_metodo_mapas_get','sintactico.py',78),
  ('metodo_mapas -> PAR_IZQ GET estructura_mapa NOMBRE PAR_DER','metodo_mapas',5,'p_metodo_mapas_get','sintactico.py',79),
  ('metodo_mapas -> PAR_IZQ GET NOMBRE NOMBRE PAR_DER','metodo_mapas',5,'p_metodo_mapas_get','sintactico.py',80),
  ('metodo_mapas -> PAR_IZQ GET NOMBRE STRING PAR_DER','metodo_mapas',5,'p_metodo_mapas_get','sintactico.py',81),
  ('metodo_mapas -> PAR_IZQ KEYS estructura_mapa PAR_DER','metodo_mapas',4,'p_metodo_mapas_conj','sintactico.py',86),
  ('metodo_mapas -> PAR_IZQ KEYS NOMBRE PAR_DER','metodo_mapas',4,'p_metodo_mapas_conj','sintactico.py',87),
  ('variable -> PAR_IZQ DEF NOMBRE expresion PAR_DER','variable',5,'p_variable','sintactico.py',91),
  ('expresion -> valor','expresion',1,'p_expresion','sintactico.py',95),
  ('expresion -> estructura','expresion',1,'p_expresion','sintactico.py',96),
  ('expresion -> expresionAritmetica','expresion',1,'p_expresion','sintactico.py',97),
  ('expresion -> comparacion','expresion',1,'p_expresion','sintactico.py',98),
  ('expresion -> comparacionLogica','expresion',1,'p_expresion','sintactico.py',99),
  ('expresion -> input','expresion',1,'p_expresion','sintactico.py',100),
  ('estructura -> estructura_mapa','estructura',1,'p_estructura','sintactico.py',104),
  ('estructura -> estructura_lista','estructura',1,'p_estructura','sintactico.py',105),
  ('estructura -> estructura_conjunto','estructura',1,'p_estructura','sintactico.py',106),
  ('estructura -> estructura_vector','estructura',1,'p_estructura','sintactico.py',107),
  ('estructurasControl -> if','estructurasControl',1,'p_control_estructuras','sintactico.py',112),
  ('estructurasControl -> while','estructurasControl',1,'p_control_estructuras','sintactico.py',113),
  ('estructurasControl -> loop','estructurasControl',1,'p_control_estructuras','sintactico.py',114),
  ('loop -> PAR_IZQ LOOP COR_IZQ compuesto COR_DER when PAR_DER','loop',7,'p_loop_sentencia','sintactico.py',118),
  ('when -> PAR_IZQ WHEN comparacion algoritmo recur PAR_DER','when',6,'p_when_loop_sentencia','sintactico.py',122),
  ('recur -> PAR_IZQ RECUR expresionAritmetica PAR_DER','recur',4,'p_recur_loop_sentencia','sintactico.py',126),
  ('while -> PAR_IZQ WHILE comparacion PAR_IZQ DO sentencia_compuesta PAR_DER PAR_DER','while',8,'p_while_sentencia','sintactico.py',130),
  ('if -> PAR_IZQ IF expresionBooleana sentencia_compuesta PAR_DER','if',5,'p_if_sentencia','sintactico.py',134),
  ('expresionBooleana -> FALSE','expresionBooleana',1,'p_boolean_expresion','sintactico.py',137),
  ('expresionBooleana -> TRUE','expresionBooleana',1,'p_boolean_expresion','sintactico.py',138),
  ('expresionBooleana -> comparacionLogica','expresionBooleana',1,'p_boolean_expresion','sintactico.py',139),
  ('expresionBooleana -> comparacion','expresionBooleana',1,'p_boolean_expresion','sintactico.py',140),
  ('input -> PAR_IZQ READ REST LINE PAR_DER','input',5,'p_input','sintactico.py',144),
  ('imprimir -> PAR_IZQ opcionesImprimir expresion PAR_DER','imprimir',4,'p_imprimir','sintactico.py',147),
  ('comparacionLogica -> PAR_IZQ operadorLogico valor valor PAR_DER','comparacionLogica',5,'p_comparacion_logica','sintactico.py',151),
  ('comparacionLogica -> PAR_IZQ NOT valor PAR_DER','comparacionLogica',4,'p_comparacion_logica','sintactico.py',152),
  ('comparacion -> PAR_IZQ operadorComparacion valor valor PAR_DER','comparacion',5,'p_comparacion','sintactico.py',156),
  ('expresionAritmetica -> PAR_IZQ operadorMat numberoSerie PAR_DER','expresionAritmetica',4,'p_expresion_aritmetica','sintactico.py',160),
  ('numberoSerie -> numero','numberoSerie',1,'p_numbero_serie','sintactico.py',164),
  ('numberoSerie -> NOMBRE','numberoSerie',1,'p_numbero_serie','sintactico.py',165),
  ('numberoSerie -> expresionAritmetica','numberoSerie',1,'p_numbero_serie','sintactico.py',166),
  ('numberoSerie -> numero numberoSerie','numberoSerie',2,'p_numbero_serie','sintactico.py',167),
  ('numberoSerie -> NOMBRE numberoSerie','numberoSerie',2,'p_numbero_serie','sintactico.py',168),
  ('numberoSerie -> expresionAritmetica numberoSerie','numberoSerie',2,'p_numbero_serie','sintactico.py',169),
  ('estructura_lista -> PAR_IZQ LISTA PAR_IZQ compuesto PAR_DER PAR_DER','estructura_lista',6,'p_estructura_lista','sintactico.py',175),
  ('estructura_lista -> COM_SIM PAR_IZQ compuesto PAR_DER','estructura_lista',4,'p_estructura_lista','sintactico.py',176),
  ('estructura_lista -> PAR_IZQ LISTA compuesto PAR_DER','estructura_lista',4,'p_estructura_lista','sintactico.py',177),
  ('estructura_conjunto -> PAR_IZQ CONJUNTO COM_SIM PAR_IZQ compuesto PAR_DER PAR_DER','estructura_conjunto',7,'p_estructura_conjunto','sintactico.py',181),
  ('estructura_conjunto -> HASH LLAV_IZQ compuesto LLAV_DER','estructura_conjunto',4,'p_estructura_conjunto','sintactico.py',182),
  ('estructura_vector -> PAR_IZQ VECTOR compuesto PAR_DER','estructura_vector',4,'p_estructura_vector','sintactico.py',187),
  ('estructura_vector -> COR_IZQ compuesto COR_DER','estructura_vector',3,'p_estructura_vector','sintactico.py',188),
  ('estructura_mapa -> LLAV_IZQ parclaves LLAV_DER','estructura_mapa',3,'p_estructura_mapa','sintactico.py',193),
  ('estructura_mapa -> PAR_IZQ mapas parclaves PAR_DER','estructura_mapa',4,'p_estructura_mapa','sintactico.py',194),
  ('mapas -> SORTEDMAP REST MAP','mapas',3,'p_mapas','sintactico.py',198),
  ('mapas -> HASHMAP REST MAP','mapas',3,'p_mapas','sintactico.py',199),
  ('compuesto -> valor','compuesto',1,'p_compuesto','sintactico.py',203),
  ('compuesto -> valor compuesto','compuesto',2,'p_compuesto','sintactico.py',204),
  ('parclaves -> STRING STRING','parclaves',2,'p_parclaves','sintactico.py',208),
  ('parclaves -> STRING STRING COMA parclaves','parclaves',4,'p_parclaves','sintactico.py',209),
  ('parclaves -> STRING STRING parclaves','parclaves',3,'p_parclaves','sintactico.py',210),
  ('valor -> numero','valor',1,'p_valor','sintactico.py',214),
  ('valor -> NOMBRE','valor',1,'p_valor','sintactico.py',215),
  ('valor -> booleano','valor',1,'p_valor','sintactico.py',216),
  ('valor -> cadena','valor',1,'p_valor','sintactico.py',217),
  ('cadena -> STRING','cadena',1,'p_cadena','sintactico.py',221),
  ('cadena -> PAR_IZQ STR STRING STRING PAR_DER','cadena',5,'p_cadena','sintactico.py',222),
  ('booleano -> TRUE','booleano',1,'p_booleano','sintactico.py',226),
  ('booleano -> FALSE','booleano',1,'p_booleano','sintactico.py',227),
  ('numero -> ENTERO','numero',1,'p_numero','sintactico.py',231),
  ('numero -> FLOTANTE','numero',1,'p_numero','sintactico.py',232),
  ('operadorMat -> SUM','operadorMat',1,'p_operador_mat','sintactico.py',237),
  ('operadorMat -> REST','operadorMat',1,'p_operador_mat','sintactico.py',238),
  ('operadorMat -> PRODUCT','operadorMat',1,'p_operador_mat','sintactico.py',239),
  ('operadorMat -> DIVISION','operadorMat',1,'p_operador_mat','sintactico.py',240),
  ('operadorComparacion -> EQUAL','operadorComparacion',1,'p_operador_comparacion','sintactico.py',245),
  ('operadorComparacion -> NOT_EQUAL','operadorComparacion',1,'p_operador_comparacion','sintactico.py',246),
  ('operadorComparacion -> GREATER_THAN','operadorComparacion',1,'p_operador_comparacion','sintactico.py',247),
  ('operadorComparacion -> LESS_THAN','operadorComparacion',1,'p_operador_comparacion','sintactico.py',248),
  ('operadorComparacion -> GREATER_THAN_EQUAL','operadorComparacion',1,'p_operador_comparacion','sintactico.py',249),
  ('operadorComparacion -> LESS_THAN_EQUAL','operadorComparacion',1,'p_operador_comparacion','sintactico.py',250),
  ('operadorLogico -> AND','operadorLogico',1,'p_operador_logico','sintactico.py',254),
  ('operadorLogico -> OR','operadorLogico',1,'p_operador_logico','sintactico.py',255),
  ('opcionesImprimir -> PRINT','opcionesImprimir',1,'p_imprimir_opciones','sintactico.py',259),
  ('opcionesImprimir -> PRINTLN','opcionesImprimir',1,'p_imprimir_opciones','sintactico.py',260),
]
