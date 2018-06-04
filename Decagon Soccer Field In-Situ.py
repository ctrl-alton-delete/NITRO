import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

%matplotlib qt4

matplotlib.style.use('meter-blue')

def get_text_from_figure(figure):
    texts = []
    for x in figure.get_default_bbox_extra_artists():
        if type(x) is matplotlib.text.Text:
            texts.append(x)
    return texts

def apply_meter_blue(figure):
    meter_blue = '#03528a'
    meter_fifty = '#98adc7'
    meter_thirty = '#c0cbde'
    for ax in fig.get_axes():
        ax.tick_params(axis='both',which='both',top=False,right=False,color=meter_thirty)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    for x in get_text_from_figure(fig):
        x.set_color(meter_blue)
    return None

df = pd.read_excel('C:\\Users\\Alton\\Desktop\\Pullman Soccer Field In-Situ .xls',index_col=0,na_values=['#N/A','***'])
df.head()

df=df.resample('30T').mean()

fig = plt.figure(num=1)
under_500 = -df['5cm Potential'] <= 500
drying = (df['5cm Potential'].diff() <= 0)&(df['5cm VWC'].diff() <= 0)

ax1 = fig.add_subplot(111)
ax1.plot(-df['5cm Potential'][under_500 & drying],df['5cm VWC'][under_500 & drying],'.',label='5cm MRC')
ax1.legend()
apply_meter_blue(fig)
fig.show()
