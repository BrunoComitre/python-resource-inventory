# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:05:04 2018

@author: bruno
"""

#EXERCÍCIO 21 - Abra e reproduza o áudio de um arquivo MP3.
 
import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
