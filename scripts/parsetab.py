
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DEF NULL HASHMAP SORTEDMAP MAP VECTOR CONJUNTO STR LOOP WHILE DO WHEN PRINTLN PRINT RECUR DEFN FIRST LISTA NTH IF DOSEQ TRUE FALSE READLINE NOT AND OR CONS GET CONJ KEYS ENTERO FLOTANTE CHAR STRING PAR_DER PAR_IZQ COR_DER COR_IZQ SUM REST PRODUCT DIVISION EQUAL NOT_EQUAL GREATER_THAN LESS_THAN GREATER_THAN_EQUAL LESS_THAN_EQUAL COM_SIM NOMBRE HASH LLAV_IZQ LLAV_DERsentencia_compuesta : algoritmo\n                            | algoritmo sentencia_compuesta\n    algoritmo : variable\n                 | expresion\n                 | imprimir\n                 | controlStructures\n                 | funcion\n                 | metodo_lista\n                 | metodo_conjunto\n                 | metodo_vector\n                 | metodo_mapas\n    funcion : PAR_IZQ DEFN NOMBRE argumentos sentencia_compuesta PAR_DERargumentos :  COR_IZQ argumento COR_DER\n                  | COR_IZQ COR_DER\n    argumento : NOMBRE\n                 | NOMBRE argumento\n    metodo_lista : PAR_IZQ FIRST NOMBRE PAR_DER\n                    | PAR_IZQ FIRST estructura_lista PAR_DERmetodo_lista : PAR_IZQ NTH NOMBRE NOMBRE PAR_DER\n                    | PAR_IZQ NTH NOMBRE ENTERO PAR_DER\n                    | PAR_IZQ NTH estructura_lista ENTERO PAR_DER\n                    | PAR_IZQ NTH estructura_lista NOMBRE PAR_DERmetodo_lista : PAR_IZQ CONS valor NOMBRE PAR_DER\n                    | PAR_IZQ CONS valor estructura_lista PAR_DERmetodo_conjunto : PAR_IZQ GET estructura_conjunto NOMBRE PAR_DER\n                        | PAR_IZQ GET estructura_conjunto ENTERO PAR_DER\n    metodo_conjunto : PAR_IZQ CONJ estructura_conjunto valor PAR_DERmetodo_vector : PAR_IZQ GET estructura_vector NOMBRE PAR_DER\n                        | PAR_IZQ GET estructura_vector ENTERO PAR_DER\n    metodo_vector : PAR_IZQ CONJ estructura_vector valor PAR_DERmetodo_mapas : PAR_IZQ GET estructura_mapa STRING PAR_DER\n                    | PAR_IZQ GET estructura_mapa NOMBRE PAR_DER\n                    | PAR_IZQ GET NOMBRE NOMBRE PAR_DER\n                    | PAR_IZQ GET NOMBRE STRING PAR_DER\n    metodo_mapas : PAR_IZQ KEYS estructura_mapa PAR_DER\n                    | PAR_IZQ KEYS NOMBRE PAR_DERvariable : PAR_IZQ DEF NOMBRE expresion PAR_DERexpresion : valor\n                 | estructura\n                 | expresionAritmetica\n                 | comparation\n                 | comparationLogic\n    estructura : estructura_mapa\n                  | estructura_lista\n                  | estructura_conjunto\n                  | estructura_vector controlStructures : if\n                          | while\n                          | loop\n    loop : PAR_IZQ LOOP COR_IZQ compuesto COR_DER when PAR_DER\n    when : PAR_IZQ WHEN comparation algoritmo recur PAR_DER\n    recur : PAR_IZQ RECUR expresionAritmetica PAR_DER\n    while : PAR_IZQ WHILE comparation PAR_IZQ DO sentencia_compuesta PAR_DER PAR_DER\n    if : PAR_IZQ IF booleanExpresion sentencia_compuesta PAR_DERbooleanExpresion : FALSE\n                        | TRUE\n                        | comparationLogic\n                        | comparation\n    imprimir : PAR_IZQ imprimirOptions expresion PAR_DER\n    comparationLogic :  PAR_IZQ operadorLogic valor valor PAR_DER\n                      | PAR_IZQ NOT valor PAR_DER\n    comparation : PAR_IZQ operadorCompare valor valor PAR_DERexpresionAritmetica : PAR_IZQ operadorMath numberSerie PAR_DER\n    numberSerie : numero\n                    | NOMBRE\n                    | expresionAritmetica\n                    | numero numberSerie\n                    | NOMBRE numberSerie\n                    | expresionAritmetica numberSerie\n    estructura_lista : PAR_IZQ LISTA PAR_IZQ compuesto PAR_DER PAR_DER\n                  | COM_SIM PAR_IZQ compuesto PAR_DER\n                  | PAR_IZQ LISTA compuesto PAR_DER\n    estructura_conjunto : PAR_IZQ CONJUNTO COM_SIM PAR_IZQ compuesto PAR_DER PAR_DER\n                  | HASH LLAV_IZQ compuesto LLAV_DER\n    estructura_vector : PAR_IZQ VECTOR compuesto PAR_DER\n                  | COR_IZQ compuesto COR_DER\n    estructura_mapa : LLAV_IZQ parclaves LLAV_DER\n                  | PAR_IZQ mapas parclaves PAR_DER\n    mapas : SORTEDMAP REST MAP\n             | HASHMAP REST MAP\n    compuesto : valor\n                 | valor compuesto\n    parclaves : STRING STRING\n                 | STRING STRING parclaves\n    valor : numero\n             | NOMBRE\n             | booleano\n             | cadena\n    cadena : STRING\n              | PAR_IZQ STR STRING STRING PAR_DER\n    booleano : TRUE\n                | FALSE\n    numero : ENTERO\n              | FLOTANTE\n    operadorMath : SUM\n                    | REST\n                    | PRODUCT\n                    | DIVISION\n    operadorCompare : EQUAL\n                        | NOT_EQUAL\n                        | GREATER_THAN\n                        | LESS_THAN\n                        | GREATER_THAN_EQUAL\n                        | LESS_THAN_EQUAL\n    operadorLogic : AND\n                     | OR\n    imprimirOptions : PRINT\n                        | PRINTLN\n    '
    
_lr_action_items = {'PAR_IZQ':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,40,42,43,44,45,46,47,48,49,50,51,52,53,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,77,81,82,83,92,99,100,106,107,108,109,110,113,114,115,116,117,119,120,123,125,129,131,136,137,139,140,157,158,159,165,170,172,173,174,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,209,210,215,218,219,220,221,222,223,226,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,78,-94,-91,-92,81,84,87,87,78,93,98,101,104,78,78,78,112,118,123,78,-107,-108,-95,-96,-97,-98,-99,-100,-101,-102,-103,-104,-105,-106,78,78,78,84,87,78,78,104,104,104,78,78,12,-55,-56,-57,-58,167,78,78,173,-76,-77,-59,12,-17,-18,-35,-36,-63,-61,-78,-72,78,-75,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,12,213,-90,-12,-13,-70,118,-50,-73,-53,12,224,104,]),'NOMBRE':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,47,48,49,50,51,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,77,81,82,83,90,91,92,94,95,96,97,99,100,106,107,108,109,110,113,114,115,116,117,120,123,129,131,136,137,138,139,140,157,158,159,165,170,172,173,174,178,179,180,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,13,-94,-91,-92,83,13,86,88,90,13,95,103,107,13,13,13,13,13,-107,-108,-95,-96,-97,-98,-99,-100,-101,-102,-103,-104,-105,-106,13,13,13,13,141,144,145,147,149,151,154,13,13,107,107,107,13,13,13,-55,-56,-57,-58,13,13,-76,-77,-59,13,184,-17,-18,-35,-36,-63,-61,-78,-72,13,-75,-71,-74,-37,-14,184,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,13,-90,-12,-13,-70,-50,-73,-53,13,]),'ENTERO':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,40,44,48,49,50,51,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,77,81,82,83,90,91,94,96,99,100,106,107,108,109,110,113,114,115,116,117,120,123,129,131,136,137,139,140,157,158,159,165,170,172,173,174,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,23,-94,-91,-92,23,23,23,23,23,23,23,23,-107,-108,-95,-96,-97,-98,-99,-100,-101,-102,-103,-104,-105,-106,23,23,23,23,142,143,148,152,23,23,23,23,23,23,23,23,-55,-56,-57,-58,23,23,-76,-77,-59,23,-17,-18,-35,-36,-63,-61,-78,-72,23,-75,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,23,-90,-12,-13,-70,-50,-73,-53,23,]),'FLOTANTE':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,40,44,48,49,50,51,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,77,81,82,83,99,100,106,107,108,109,110,113,114,115,116,117,120,123,129,131,136,137,139,140,157,158,159,165,170,172,173,174,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[32,32,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,32,-94,-91,-92,32,32,32,32,32,32,32,32,-107,-108,-95,-96,-97,-98,-99,-100,-101,-102,-103,-104,-105,-106,32,32,32,32,32,32,32,32,32,32,32,32,-55,-56,-57,-58,32,32,-76,-77,-59,32,-17,-18,-35,-36,-63,-61,-78,-72,32,-75,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,32,-90,-12,-13,-70,-50,-73,-53,32,]),'TRUE':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,40,44,49,50,51,52,57,59,60,61,66,67,68,69,70,71,72,73,77,81,82,83,99,100,109,110,113,114,115,116,117,120,123,129,131,136,137,139,140,157,158,159,165,170,172,173,174,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[33,33,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,33,-94,-91,-92,33,33,33,33,33,115,33,33,-107,-108,-99,-100,-101,-102,-103,-104,-105,-106,33,33,33,33,33,33,33,33,33,-55,-56,-57,-58,33,33,-76,-77,-59,33,-17,-18,-35,-36,-63,-61,-78,-72,33,-75,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,33,-90,-12,-13,-70,-50,-73,-53,33,]),'FALSE':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,40,44,49,50,51,52,57,59,60,61,66,67,68,69,70,71,72,73,77,81,82,83,99,100,109,110,113,114,115,116,117,120,123,129,131,136,137,139,140,157,158,159,165,170,172,173,174,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[34,34,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,34,-94,-91,-92,34,34,34,34,34,114,34,34,-107,-108,-99,-100,-101,-102,-103,-104,-105,-106,34,34,34,34,34,34,34,34,34,-55,-56,-57,-58,34,34,-76,-77,-59,34,-17,-18,-35,-36,-63,-61,-78,-72,34,-75,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,34,-90,-12,-13,-70,-50,-73,-53,34,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,40,44,49,50,51,55,56,57,59,60,61,66,67,68,69,70,71,72,73,77,80,81,82,83,95,97,99,100,109,110,113,114,115,116,117,120,121,123,129,131,132,136,137,139,140,157,158,159,165,170,172,173,174,175,176,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,27,-94,-91,-92,80,27,27,27,27,27,121,80,27,27,-107,-108,-99,-100,-101,-102,-103,-104,-105,-106,27,132,27,27,27,150,153,27,27,27,27,27,-55,-56,-57,-58,27,169,27,-76,-77,80,-59,27,-17,-18,-35,-36,-63,-61,-78,-72,27,-75,-79,-80,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,27,-90,-12,-13,-70,-50,-73,-53,27,]),'LLAV_IZQ':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,37,40,45,47,60,61,83,113,114,115,116,117,129,131,136,137,139,140,157,158,159,165,170,172,174,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[35,35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,-94,-91,-92,82,35,35,35,-107,-108,35,35,-55,-56,-57,-58,-76,-77,-59,35,-17,-18,-35,-36,-63,-61,-78,-72,-75,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,35,-90,-12,-13,-70,-50,-73,-53,35,]),'COM_SIM':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,40,42,43,58,60,61,83,92,113,114,115,116,117,129,131,136,137,139,140,157,158,159,165,170,172,174,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[36,36,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,-94,-91,-92,36,36,36,125,-107,-108,36,36,36,-55,-56,-57,-58,-76,-77,-59,36,-17,-18,-35,-36,-63,-61,-78,-72,-75,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,36,-90,-12,-13,-70,-50,-73,-53,36,]),'HASH':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,40,45,46,60,61,83,113,114,115,116,117,129,131,136,137,139,140,157,158,159,165,170,172,174,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[37,37,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,-94,-91,-92,37,37,37,-107,-108,37,37,-55,-56,-57,-58,-76,-77,-59,37,-17,-18,-35,-36,-63,-61,-78,-72,-75,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,37,-90,-12,-13,-70,-50,-73,-53,37,]),'COR_IZQ':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,40,45,46,54,60,61,83,86,113,114,115,116,117,129,131,136,137,139,140,157,158,159,165,170,172,174,178,179,180,183,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,209,210,215,219,220,221,222,],[31,31,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,-94,-91,-92,31,31,31,120,-107,-108,31,138,31,-55,-56,-57,-58,-76,-77,-59,31,-17,-18,-35,-36,-63,-61,-78,-72,-75,-71,-74,-37,-14,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,31,-90,-12,-13,-70,-50,-73,-53,31,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,38,129,131,136,139,140,157,158,159,165,170,172,174,178,179,180,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,206,209,215,219,220,221,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,-94,-91,-92,-2,-76,-77,-59,-17,-18,-35,-36,-63,-61,-78,-72,-75,-71,-74,-37,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,-90,-12,-70,-50,-73,-53,]),'PAR_DER':([2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,38,77,85,88,89,102,103,105,106,107,108,111,122,124,126,129,130,131,132,133,135,136,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,169,170,171,172,174,177,178,179,180,181,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,206,207,208,209,212,214,215,216,217,219,220,221,225,227,228,229,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-86,-38,-39,-40,-41,-42,-47,-48,-49,-44,-93,-45,-46,-43,-89,-85,-87,-88,-94,-91,-92,-2,-81,136,139,140,157,158,159,-64,-65,-66,165,170,172,174,-76,-82,-77,-83,178,180,-59,-17,-18,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,-35,-36,-63,-67,-68,-69,201,202,-61,203,206,-78,207,-72,-75,-84,-71,-74,-37,209,-19,-20,-21,-22,-23,-24,-25,-26,-33,-34,-28,-29,-31,-32,-27,-30,-62,-60,-54,-90,215,216,-12,217,219,-70,220,221,-50,-73,-53,227,-51,229,-52,]),'DEF':([12,],[39,]),'DEFN':([12,],[41,]),'FIRST':([12,],[42,]),'NTH':([12,],[43,]),'CONS':([12,],[44,]),'GET':([12,],[45,]),'CONJ':([12,],[46,]),'KEYS':([12,],[47,]),'NOT':([12,84,112,],[51,51,51,]),'IF':([12,],[52,]),'WHILE':([12,],[53,]),'LOOP':([12,],[54,]),'STR':([12,78,84,123,],[55,55,55,55,]),'LISTA':([12,84,87,],[57,57,57,]),'CONJUNTO':([12,84,93,98,],[58,58,58,58,]),'VECTOR':([12,84,93,98,],[59,59,59,59,]),'PRINT':([12,],[60,]),'PRINTLN':([12,],[61,]),'SUM':([12,84,104,],[62,62,62,]),'REST':([12,74,75,84,104,],[63,127,128,63,63,]),'PRODUCT':([12,84,104,],[64,64,64,]),'DIVISION':([12,84,104,],[65,65,65,]),'EQUAL':([12,84,112,118,],[66,66,66,66,]),'NOT_EQUAL':([12,84,112,118,],[67,67,67,67,]),'GREATER_THAN':([12,84,112,118,],[68,68,68,68,]),'LESS_THAN':([12,84,112,118,],[69,69,69,69,]),'GREATER_THAN_EQUAL':([12,84,112,118,],[70,70,70,70,]),'LESS_THAN_EQUAL':([12,84,112,118,],[71,71,71,71,]),'AND':([12,84,112,],[72,72,72,]),'OR':([12,84,112,],[73,73,73,]),'SORTEDMAP':([12,84,93,101,],[74,74,74,74,]),'HASHMAP':([12,84,93,101,],[75,75,75,75,]),'COR_DER':([13,23,27,28,29,30,32,33,34,76,77,130,138,168,182,184,206,211,],[-86,-93,-89,-85,-87,-88,-94,-91,-92,129,-81,-82,183,205,210,-15,-90,-16,]),'LLAV_DER':([13,23,27,28,29,30,32,33,34,77,79,130,132,134,177,206,],[-86,-93,-89,-85,-87,-88,-94,-91,-92,-81,131,-82,-83,179,-84,-90,]),'MAP':([127,128,],[175,176,]),'DO':([167,],[204,]),'WHEN':([213,],[218,]),'RECUR':([224,],[226,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia_compuesta':([0,2,113,137,204,],[1,38,166,181,212,]),'algoritmo':([0,2,113,137,204,222,],[2,2,2,2,2,223,]),'variable':([0,2,113,137,204,222,],[3,3,3,3,3,3,]),'expresion':([0,2,40,83,113,137,204,222,],[4,4,85,135,4,4,4,4,]),'imprimir':([0,2,113,137,204,222,],[5,5,5,5,5,5,]),'controlStructures':([0,2,113,137,204,222,],[6,6,6,6,6,6,]),'funcion':([0,2,113,137,204,222,],[7,7,7,7,7,7,]),'metodo_lista':([0,2,113,137,204,222,],[8,8,8,8,8,8,]),'metodo_conjunto':([0,2,113,137,204,222,],[9,9,9,9,9,9,]),'metodo_vector':([0,2,113,137,204,222,],[10,10,10,10,10,10,]),'metodo_mapas':([0,2,113,137,204,222,],[11,11,11,11,11,11,]),'valor':([0,2,31,40,44,49,50,51,57,59,77,81,82,83,99,100,109,110,113,120,123,137,173,204,222,],[14,14,77,14,92,109,110,111,77,77,77,77,77,14,155,156,163,164,14,77,77,14,77,14,14,]),'estructura':([0,2,40,83,113,137,204,222,],[15,15,15,15,15,15,15,15,]),'expresionAritmetica':([0,2,40,48,83,106,107,108,113,137,204,222,226,],[16,16,16,108,16,108,108,108,16,16,16,16,228,]),'comparation':([0,2,40,52,53,83,113,137,204,218,222,],[17,17,17,117,119,17,17,17,17,222,17,]),'comparationLogic':([0,2,40,52,83,113,137,204,222,],[18,18,18,116,18,18,18,18,18,]),'if':([0,2,113,137,204,222,],[19,19,19,19,19,19,]),'while':([0,2,113,137,204,222,],[20,20,20,20,20,20,]),'loop':([0,2,113,137,204,222,],[21,21,21,21,21,21,]),'estructura_lista':([0,2,40,42,43,83,92,113,137,204,222,],[22,22,22,89,91,22,146,22,22,22,22,]),'estructura_conjunto':([0,2,40,45,46,83,113,137,204,222,],[24,24,24,94,99,24,24,24,24,24,]),'estructura_vector':([0,2,40,45,46,83,113,137,204,222,],[25,25,25,96,100,25,25,25,25,25,]),'estructura_mapa':([0,2,40,45,47,83,113,137,204,222,],[26,26,26,97,102,26,26,26,26,26,]),'numero':([0,2,31,40,44,48,49,50,51,57,59,77,81,82,83,99,100,106,107,108,109,110,113,120,123,137,173,204,222,],[28,28,28,28,28,106,28,28,28,28,28,28,28,28,28,28,28,106,106,106,28,28,28,28,28,28,28,28,28,]),'booleano':([0,2,31,40,44,49,50,51,57,59,77,81,82,83,99,100,109,110,113,120,123,137,173,204,222,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'cadena':([0,2,31,40,44,49,50,51,57,59,77,81,82,83,99,100,109,110,113,120,123,137,173,204,222,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'imprimirOptions':([12,],[40,]),'operadorMath':([12,84,104,],[48,48,48,]),'operadorCompare':([12,84,112,118,],[49,49,49,49,]),'operadorLogic':([12,84,112,],[50,50,50,]),'mapas':([12,84,93,101,],[56,56,56,56,]),'compuesto':([31,57,59,77,81,82,120,123,173,],[76,124,126,130,133,134,168,171,208,]),'parclaves':([35,56,132,],[79,122,177,]),'numberSerie':([48,106,107,108,],[105,160,161,162,]),'booleanExpresion':([52,],[113,]),'argumentos':([86,],[137,]),'argumento':([138,184,],[182,211,]),'when':([205,],[214,]),'recur':([223,],[225,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencia_compuesta","S'",1,None,None,None),
  ('sentencia_compuesta -> algoritmo','sentencia_compuesta',1,'p_sentencia_compuesta','sintactico.py',7),
  ('sentencia_compuesta -> algoritmo sentencia_compuesta','sentencia_compuesta',2,'p_sentencia_compuesta','sintactico.py',8),
  ('algoritmo -> variable','algoritmo',1,'p_algoritmo','sintactico.py',12),
  ('algoritmo -> expresion','algoritmo',1,'p_algoritmo','sintactico.py',13),
  ('algoritmo -> imprimir','algoritmo',1,'p_algoritmo','sintactico.py',14),
  ('algoritmo -> controlStructures','algoritmo',1,'p_algoritmo','sintactico.py',15),
  ('algoritmo -> funcion','algoritmo',1,'p_algoritmo','sintactico.py',16),
  ('algoritmo -> metodo_lista','algoritmo',1,'p_algoritmo','sintactico.py',17),
  ('algoritmo -> metodo_conjunto','algoritmo',1,'p_algoritmo','sintactico.py',18),
  ('algoritmo -> metodo_vector','algoritmo',1,'p_algoritmo','sintactico.py',19),
  ('algoritmo -> metodo_mapas','algoritmo',1,'p_algoritmo','sintactico.py',20),
  ('funcion -> PAR_IZQ DEFN NOMBRE argumentos sentencia_compuesta PAR_DER','funcion',6,'p_funcion','sintactico.py',25),
  ('argumentos -> COR_IZQ argumento COR_DER','argumentos',3,'p_argumentos','sintactico.py',28),
  ('argumentos -> COR_IZQ COR_DER','argumentos',2,'p_argumentos','sintactico.py',29),
  ('argumento -> NOMBRE','argumento',1,'p_argumento','sintactico.py',33),
  ('argumento -> NOMBRE argumento','argumento',2,'p_argumento','sintactico.py',34),
  ('metodo_lista -> PAR_IZQ FIRST NOMBRE PAR_DER','metodo_lista',4,'p_metodo_lista_first','sintactico.py',39),
  ('metodo_lista -> PAR_IZQ FIRST estructura_lista PAR_DER','metodo_lista',4,'p_metodo_lista_first','sintactico.py',40),
  ('metodo_lista -> PAR_IZQ NTH NOMBRE NOMBRE PAR_DER','metodo_lista',5,'p_metodo_lista_nth','sintactico.py',44),
  ('metodo_lista -> PAR_IZQ NTH NOMBRE ENTERO PAR_DER','metodo_lista',5,'p_metodo_lista_nth','sintactico.py',45),
  ('metodo_lista -> PAR_IZQ NTH estructura_lista ENTERO PAR_DER','metodo_lista',5,'p_metodo_lista_nth','sintactico.py',46),
  ('metodo_lista -> PAR_IZQ NTH estructura_lista NOMBRE PAR_DER','metodo_lista',5,'p_metodo_lista_nth','sintactico.py',47),
  ('metodo_lista -> PAR_IZQ CONS valor NOMBRE PAR_DER','metodo_lista',5,'p_metodo_lista_cons','sintactico.py',51),
  ('metodo_lista -> PAR_IZQ CONS valor estructura_lista PAR_DER','metodo_lista',5,'p_metodo_lista_cons','sintactico.py',52),
  ('metodo_conjunto -> PAR_IZQ GET estructura_conjunto NOMBRE PAR_DER','metodo_conjunto',5,'p_metodo_conjunto_get','sintactico.py',57),
  ('metodo_conjunto -> PAR_IZQ GET estructura_conjunto ENTERO PAR_DER','metodo_conjunto',5,'p_metodo_conjunto_get','sintactico.py',58),
  ('metodo_conjunto -> PAR_IZQ CONJ estructura_conjunto valor PAR_DER','metodo_conjunto',5,'p_metodo_conjunto_conj','sintactico.py',63),
  ('metodo_vector -> PAR_IZQ GET estructura_vector NOMBRE PAR_DER','metodo_vector',5,'p_metodo_vector_get','sintactico.py',68),
  ('metodo_vector -> PAR_IZQ GET estructura_vector ENTERO PAR_DER','metodo_vector',5,'p_metodo_vector_get','sintactico.py',69),
  ('metodo_vector -> PAR_IZQ CONJ estructura_vector valor PAR_DER','metodo_vector',5,'p_metodo_vector_conj','sintactico.py',74),
  ('metodo_mapas -> PAR_IZQ GET estructura_mapa STRING PAR_DER','metodo_mapas',5,'p_metodo_mapas_get','sintactico.py',79),
  ('metodo_mapas -> PAR_IZQ GET estructura_mapa NOMBRE PAR_DER','metodo_mapas',5,'p_metodo_mapas_get','sintactico.py',80),
  ('metodo_mapas -> PAR_IZQ GET NOMBRE NOMBRE PAR_DER','metodo_mapas',5,'p_metodo_mapas_get','sintactico.py',81),
  ('metodo_mapas -> PAR_IZQ GET NOMBRE STRING PAR_DER','metodo_mapas',5,'p_metodo_mapas_get','sintactico.py',82),
  ('metodo_mapas -> PAR_IZQ KEYS estructura_mapa PAR_DER','metodo_mapas',4,'p_metodo_mapas_conj','sintactico.py',87),
  ('metodo_mapas -> PAR_IZQ KEYS NOMBRE PAR_DER','metodo_mapas',4,'p_metodo_mapas_conj','sintactico.py',88),
  ('variable -> PAR_IZQ DEF NOMBRE expresion PAR_DER','variable',5,'p_variable','sintactico.py',92),
  ('expresion -> valor','expresion',1,'p_expresion','sintactico.py',96),
  ('expresion -> estructura','expresion',1,'p_expresion','sintactico.py',97),
  ('expresion -> expresionAritmetica','expresion',1,'p_expresion','sintactico.py',98),
  ('expresion -> comparation','expresion',1,'p_expresion','sintactico.py',99),
  ('expresion -> comparationLogic','expresion',1,'p_expresion','sintactico.py',100),
  ('estructura -> estructura_mapa','estructura',1,'p_estructura','sintactico.py',104),
  ('estructura -> estructura_lista','estructura',1,'p_estructura','sintactico.py',105),
  ('estructura -> estructura_conjunto','estructura',1,'p_estructura','sintactico.py',106),
  ('estructura -> estructura_vector','estructura',1,'p_estructura','sintactico.py',107),
  ('controlStructures -> if','controlStructures',1,'p_control_structures','sintactico.py',112),
  ('controlStructures -> while','controlStructures',1,'p_control_structures','sintactico.py',113),
  ('controlStructures -> loop','controlStructures',1,'p_control_structures','sintactico.py',114),
  ('loop -> PAR_IZQ LOOP COR_IZQ compuesto COR_DER when PAR_DER','loop',7,'p_loop_statement','sintactico.py',118),
  ('when -> PAR_IZQ WHEN comparation algoritmo recur PAR_DER','when',6,'p_when_loop_statement','sintactico.py',122),
  ('recur -> PAR_IZQ RECUR expresionAritmetica PAR_DER','recur',4,'p_recur_loop_statement','sintactico.py',126),
  ('while -> PAR_IZQ WHILE comparation PAR_IZQ DO sentencia_compuesta PAR_DER PAR_DER','while',8,'p_while_statement','sintactico.py',130),
  ('if -> PAR_IZQ IF booleanExpresion sentencia_compuesta PAR_DER','if',5,'p_if_statement','sintactico.py',134),
  ('booleanExpresion -> FALSE','booleanExpresion',1,'p_boolean_expresion','sintactico.py',137),
  ('booleanExpresion -> TRUE','booleanExpresion',1,'p_boolean_expresion','sintactico.py',138),
  ('booleanExpresion -> comparationLogic','booleanExpresion',1,'p_boolean_expresion','sintactico.py',139),
  ('booleanExpresion -> comparation','booleanExpresion',1,'p_boolean_expresion','sintactico.py',140),
  ('imprimir -> PAR_IZQ imprimirOptions expresion PAR_DER','imprimir',4,'p_imprimir','sintactico.py',144),
  ('comparationLogic -> PAR_IZQ operadorLogic valor valor PAR_DER','comparationLogic',5,'p_comparation_logic','sintactico.py',148),
  ('comparationLogic -> PAR_IZQ NOT valor PAR_DER','comparationLogic',4,'p_comparation_logic','sintactico.py',149),
  ('comparation -> PAR_IZQ operadorCompare valor valor PAR_DER','comparation',5,'p_comparation','sintactico.py',153),
  ('expresionAritmetica -> PAR_IZQ operadorMath numberSerie PAR_DER','expresionAritmetica',4,'p_expresion_aritmetic','sintactico.py',157),
  ('numberSerie -> numero','numberSerie',1,'p_number_serie','sintactico.py',161),
  ('numberSerie -> NOMBRE','numberSerie',1,'p_number_serie','sintactico.py',162),
  ('numberSerie -> expresionAritmetica','numberSerie',1,'p_number_serie','sintactico.py',163),
  ('numberSerie -> numero numberSerie','numberSerie',2,'p_number_serie','sintactico.py',164),
  ('numberSerie -> NOMBRE numberSerie','numberSerie',2,'p_number_serie','sintactico.py',165),
  ('numberSerie -> expresionAritmetica numberSerie','numberSerie',2,'p_number_serie','sintactico.py',166),
  ('estructura_lista -> PAR_IZQ LISTA PAR_IZQ compuesto PAR_DER PAR_DER','estructura_lista',6,'p_estructura_lista','sintactico.py',172),
  ('estructura_lista -> COM_SIM PAR_IZQ compuesto PAR_DER','estructura_lista',4,'p_estructura_lista','sintactico.py',173),
  ('estructura_lista -> PAR_IZQ LISTA compuesto PAR_DER','estructura_lista',4,'p_estructura_lista','sintactico.py',174),
  ('estructura_conjunto -> PAR_IZQ CONJUNTO COM_SIM PAR_IZQ compuesto PAR_DER PAR_DER','estructura_conjunto',7,'p_estructura_conjunto','sintactico.py',178),
  ('estructura_conjunto -> HASH LLAV_IZQ compuesto LLAV_DER','estructura_conjunto',4,'p_estructura_conjunto','sintactico.py',179),
  ('estructura_vector -> PAR_IZQ VECTOR compuesto PAR_DER','estructura_vector',4,'p_estructura_vector','sintactico.py',184),
  ('estructura_vector -> COR_IZQ compuesto COR_DER','estructura_vector',3,'p_estructura_vector','sintactico.py',185),
  ('estructura_mapa -> LLAV_IZQ parclaves LLAV_DER','estructura_mapa',3,'p_estructura_mapa','sintactico.py',190),
  ('estructura_mapa -> PAR_IZQ mapas parclaves PAR_DER','estructura_mapa',4,'p_estructura_mapa','sintactico.py',191),
  ('mapas -> SORTEDMAP REST MAP','mapas',3,'p_mapas','sintactico.py',195),
  ('mapas -> HASHMAP REST MAP','mapas',3,'p_mapas','sintactico.py',196),
  ('compuesto -> valor','compuesto',1,'p_compuesto','sintactico.py',200),
  ('compuesto -> valor compuesto','compuesto',2,'p_compuesto','sintactico.py',201),
  ('parclaves -> STRING STRING','parclaves',2,'p_parclaves','sintactico.py',205),
  ('parclaves -> STRING STRING parclaves','parclaves',3,'p_parclaves','sintactico.py',206),
  ('valor -> numero','valor',1,'p_valor','sintactico.py',210),
  ('valor -> NOMBRE','valor',1,'p_valor','sintactico.py',211),
  ('valor -> booleano','valor',1,'p_valor','sintactico.py',212),
  ('valor -> cadena','valor',1,'p_valor','sintactico.py',213),
  ('cadena -> STRING','cadena',1,'p_cadena','sintactico.py',217),
  ('cadena -> PAR_IZQ STR STRING STRING PAR_DER','cadena',5,'p_cadena','sintactico.py',218),
  ('booleano -> TRUE','booleano',1,'p_booleano','sintactico.py',222),
  ('booleano -> FALSE','booleano',1,'p_booleano','sintactico.py',223),
  ('numero -> ENTERO','numero',1,'p_numero','sintactico.py',227),
  ('numero -> FLOTANTE','numero',1,'p_numero','sintactico.py',228),
  ('operadorMath -> SUM','operadorMath',1,'p_operador_math','sintactico.py',233),
  ('operadorMath -> REST','operadorMath',1,'p_operador_math','sintactico.py',234),
  ('operadorMath -> PRODUCT','operadorMath',1,'p_operador_math','sintactico.py',235),
  ('operadorMath -> DIVISION','operadorMath',1,'p_operador_math','sintactico.py',236),
  ('operadorCompare -> EQUAL','operadorCompare',1,'p_operador_comparation','sintactico.py',241),
  ('operadorCompare -> NOT_EQUAL','operadorCompare',1,'p_operador_comparation','sintactico.py',242),
  ('operadorCompare -> GREATER_THAN','operadorCompare',1,'p_operador_comparation','sintactico.py',243),
  ('operadorCompare -> LESS_THAN','operadorCompare',1,'p_operador_comparation','sintactico.py',244),
  ('operadorCompare -> GREATER_THAN_EQUAL','operadorCompare',1,'p_operador_comparation','sintactico.py',245),
  ('operadorCompare -> LESS_THAN_EQUAL','operadorCompare',1,'p_operador_comparation','sintactico.py',246),
  ('operadorLogic -> AND','operadorLogic',1,'p_operador_logic','sintactico.py',250),
  ('operadorLogic -> OR','operadorLogic',1,'p_operador_logic','sintactico.py',251),
  ('imprimirOptions -> PRINT','imprimirOptions',1,'p_imprimir_options','sintactico.py',255),
  ('imprimirOptions -> PRINTLN','imprimirOptions',1,'p_imprimir_options','sintactico.py',256),
]
