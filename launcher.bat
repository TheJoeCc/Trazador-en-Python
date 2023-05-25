@echo off
setlocal enabledelayedexpansion
:start
cls
echo. ====================================================================================================
echo.
echo.    :!YPGBBBG5-  .YP5PPPPYJ-.       -PPP5.   :5PP?      !PP5: ?PPJ .5PPPP555PPPP!-P5P7    :5PP!
echo.  .YH00HGPPGBH?  .#00HPPB000B:     :#0000G.   500H.    .#005  P00B .GBBBH000BBBB7 5000!  .G00P.
echo. :B00#7.         .B005   7000?     P00JG00J   .B00P    Y00#.  P00B.     Y00#.      500H. P00P.
echo. 500H-  .!!!!!!. .B00P::.P00B.    ?00G -000-   !000!  .H00!   P00B.     Y00#.       P00B500P
echo. G00#.  5000000. .B0000000B7.    -H00-  500B.   Y00B. P00Y    P00B.     Y00#.       .P0000P
echo. Y000!  ..:Y000. .B00G!J#0HY.   .B000###H0005   .B00?!00B.    P00B.     Y00#.        .B00B.
echo. :G00HY-:..Y000. .B00P  :G00B.  Y00HJJJJJ50007   -00H#00-     P00B.     Y00#.         G00G
echo. .?B0000H0000#: .#00P   .500H7-000?      P00H.    Y0000Y      P00B.     Y00#.         G00B
echo.    .!?JJJ?!..   -!!.     -!!!-!!!       :!!!:    .!!!!.      .!!-      .!!-          -!!-
echo.
echo. .............. :......:.         .....           :-!!!!-.  :..:    ....: ..........  ........:.
echo. 7000000000000. G0000000HG7       Y0000J       :JB0000000J  P00G   !#00G. -00000000#. !0000000H#5.
echo. :!!!7#00P!!!!. G00G..-P000?     !00BH00-     7H00BJ!--!?!  G00B  J000J.  -000Y-!!!-  !000?.-7#00#.
echo.      B00Y     .G00P   !000?    :#00-?00B.   !0005.         P00G:P00B-    -000?       !000!   G00#:
echo.     .B00Y      G00#YYPH0B?     P00Y  G005   P00H:          P00##00G.     -000HHHHHJ  !000GY5B0HG.
echo.     .B00Y      G00HBH00B-     ?000J7750007  P00H.          P00BJ000Y.    -000PJJJJ-  !000#B00HY.
echo.     .B00Y      G00P .J00H?   -H00HHHHH00#: !000G.      .  P00G -#00B-   -0007       !000! .G00B.
echo.     .#005     .B00G   !H00P..B00G:.....#00G. 7#000B5YYP#J  G00B  :P000J. -000BPPPPP. !000!  .500H7
echo.     .5BB?      5BBY    .GBBY?BGG-      7BGB!  .75B#HHH#G!  YBB5    JBBBJ .GGGBBBBBB- -GGB-    JBBG-
echo.
echo. ====================================================================================================
pause /nul
set contador=0
:code
echo CONECTANDO AL SATELITE...
echo INDICADOR DE ESTABILIDAD: !RANDOM!
echo INDICADOR DE ESTABILIDAD: !RANDOM!
echo INDICADOR DE ESTABILIDAD: !RANDOM!
echo INDICADOR DE ESTABILIDAD: !RANDOM!
echo INDICADOR DE ESTABILIDAD: !RANDOM!
echo INDICADOR DE ESTABILIDAD: !RANDOM!
echo INDICADOR DE ESTABILIDAD: !RANDOM!
echo INDICADOR DE ESTABILIDAD: !RANDOM!
echo INDICADOR DE ESTABILIDAD: !RANDOM!
echo INDICADOR DE ESTABILIDAD: !RANDOM!
set /a contador+=1
if !contador! lss 5 (
    goto :action
)
echo FIN DEL BUCLE
:action
cd "C:\Users\%username%\Desktop"
python proyecto.py
pause
goto :start
