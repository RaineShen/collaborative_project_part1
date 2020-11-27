#!/usr/bin/env python
# coding: utf-8

# In[29]:


class change:
    def __init__(self,name,weight,calory):
        self.name=name
        self.weight=weight
        self.calory=calory
        self.weight_list=[]
        self.calory_list=[]
        
    def new_weight(self, new_weight):
        self.weight_list.append(new_weight)
        if len(self.weight_list)!=0 and new_weight < self.weight_list[-1]:
            d=self.weight_list[-1]-new_weight
            print("Congrats! You lost {} kg, Keep up!".format(d))
        else:
            print("Today's weight is {} kg".format(new_weight))
            

    def burned_calory(self,new_calory):
        self.calory_list.append(new_calory)
        
    
    def weight_change_plot(self):
        line_chart = pygal.Line()
        line_chart.title = 'Weight Changes '
        line_chart.x_title='Day'
        line_chart.y_title='kg'
        line_chart.add(self.name, self.weight_list)
        line_chart.x_labels = map(str, range(0,len(self.weight_list)))
        display(SVG(line_chart.render (disable_xml_declaration=True)))

    def calory_change_plot(self):
        line_chart = pygal.Line()
        line_chart.title = 'calory Changes '
        line_chart.x_title='Day'
        line_chart.y_title='kcal'
        line_chart.add(self.name, self.calory_list)
        line_chart.x_labels = map(str, range(0,len(self.calory_list)))
        display(SVG(line_chart.render (disable_xml_declaration=True)))
    
    def weight_calory_plot(self):
        bar_chart = pygal.Bar() 
        bar_chart.add('calory', self.calory_list) 
        bar_chart.add('weight', self.weight_list)
        display(SVG(bar_chart.render(disable_xml_declaration=True)))
    


        
 


# In[30]:


# C1=change("yuxuan",55.1,125)
# C1.new_weight(51)
# C1.new_weight(52)
# C1.new_weight(53)
# C1.new_weight(56)
# C1.burned_calory(123)
# C1.burned_calory(127)
# C1.burned_calory(180)
# C1.burned_calory(190)
# C1.weight_change_plot()
# C1.calory_change_plot()
# C1.weight_calory_plot()


# In[ ]:



    

