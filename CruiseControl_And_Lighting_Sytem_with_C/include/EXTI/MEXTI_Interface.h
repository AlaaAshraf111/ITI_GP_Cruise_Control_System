/*******************************************************************************************************/
/* Author            : Mohamed Ashraf                                                             	   */
/* Version           : V0.0.0                                                                          */
/* Data              : 23 May 2022                                                                     */
/* Description       : NVIC_Interface.c --> implementations                                            */
/* Module  Features  :                                                                                 */
/*      01- MNVIC_voidEnableInterrupt                                                                  */
/*      02- MNVIC_voidDisableInterrupt                                                                 */
/*      03- MNVIC_voidEnableInterruptPending                                                           */
/*      04- MNVIC_voidDisableInterruptPinding                                                          */
/*      05- MNVIC_u8IsInterruptActive                                                                  */
/*      06- MNVIC_voidInitInterruptGroup                                                               */
/*      07- MNVIC_voidSetInterruptPriority                                                             */
/*      08- MNVIC_voidGenerateSoftwareInterrupt                                                        */
/*******************************************************************************************************/

/*******************************************************************************************************/
/*	* What i sell To Customer                                                                          */
/*		*  The Archictect Give The API	                                                               */
/*						- The Name Of Function                                                         */
/*						- What is The Input                                                            */
/*						- What Is The Output                                                           */
/*						- Macro                                                                        */
/*******************************************************************************************************/

/*******************************************************************************************************/
/*                                   guard of file will call on time in .c                             */
/*******************************************************************************************************/

#include "LSTD_TYPES.h"
#include "LERROR_STATES.h"
#include "LBIT_MATH.h"

#ifndef MEXTI_INTERFACE_H_
#define MEXTI_INTERFACE_H_


typedef enum
{
	Line_0,
	Line_1,
	Line_2,
	Line_3,
	Line_4,
	Line_5,
	Line_6,
	Line_7,
	Line_8,
	Line_9,
	Line_10,
	Line_11,
	Line_12,
	Line_13,
	Line_14,
	Line_15,
}Line_t;

typedef enum
{
	RISING,
	FALLING,
	ON_CHANGE,
}Sense_t;

void MEXTI_voidInit(void);
void MEXTI_voidEnableEXTI(Line_t u8Copy_Line);
void MEXTI_voidDisableEXTI(Line_t u8Copy_Line);
void MEXTI_voidEventEnable(Line_t u8Copy_Line);
void MEXTI_voidEventDisable(Line_t u8Copy_Line);
void MEXTI_voidSenseMode(Sense_t u8Copy_Sense);
void MEXTI_voidSoftwareInterrupt(Line_t u8Copy_Line);
void MEXTI_voidPendingRegister(Line_t u8Copy_Line);
void MEXTI_voidSenseModeAndLine(Sense_t u8Copy_Sense ,Line_t u8Copy_Line );

#endif /* MEXTI_INTERFACE_H_ */
