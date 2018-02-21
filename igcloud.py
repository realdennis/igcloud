#!/usr/bin/env python3
import query
import jieba
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud

doneMessage = '''
    ==========================
    ____  ____  _   ________
   / __ \/ __ \/ | / / ____/
  / / / / / / /  |/ / __/   
 / /_/ / /_/ / /|  / /___   
/_____/\____/_/ |_/_____/   

==========================
                            
'''
startMessage = '''
  ================================
   ______________    ____  ______
  / ___/_  __/   |  / __ \/_  __/
  \__ \ / / / /| | / /_/ / / /   
 ___/ // / / ___ |/ _, _/ / /    
/____//_/ /_/  |_/_/ |_| /_/     

=============================
                                 
'''

if __name__ == '__main__':
	if len(sys.argv)<2:
		print('use : igcloud [UserID]')

	else:
		UserID=sys.argv[1]
		print(''+startMessage)

		allword=query.start(UserID)
		jieba.setLogLevel(20)
		#Don't show the jieba debug message
		seg_list=jieba.cut(allword,cut_all=False)
		wl_space_split=" ".join(seg_list)
		my_wordcloud=WordCloud(font_path="noto.otf",background_color="white",width=640, height=480, margin=2).generate(wl_space_split)
		plt.title(UserID)
		plt.imshow(my_wordcloud)
		plt.axis("off")
		plt.savefig(str(UserID)+'.png',dpi=1000)
		print(doneMessage)
		print('Done! the igcloud save as '+str(UserID)+'.png')
