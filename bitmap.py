import sys
bitmap="""
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""
print('Растровое сообщение')
print('Введите сообщение для отображения вместе с растровым изображением.')
message = input ('> ')
if message =='':
    sys.exit()

    for line in ditmap.splitlines():
        for i, bit in enumerate(line):
            if bit =='':
                print(' ',end='')
            else:
                print(message[i % len(message)],end='')
                print()