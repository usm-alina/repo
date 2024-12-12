import lightFunctions as j
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
j.crop("mercury_white.png", "white-mercury_.png")

j.crop("tungsten_blue.png", "HeatingLamp_blue_.png")
j.crop("tungsten_green.png", "HeatingLamp_green_.png")
j.crop("tungsten_red.png", "HeatingLamp_red_.png")
j.crop("tungsten_white.png", "HeatingLamp_white_.png")
j.crop("tungsten_yellow.png", "HeatingLamp_yellow_.png")

k = -0.6823907575741763
b = 643.6896231436353
mc, l = j.readIntensity("white-mercury_.png", "plot-white-mercury", "Ртутная лампа", "Белый лист")
mcb, lb = j.readIntensity("HeatingLamp_blue_.png", "plot-blue-heating", "Лампа накаливания", "Синий лист")
mcg, lg = j.readIntensity("HeatingLamp_green_.png", "plot-green-heating", "Лампа накаливания", "Зелёный лист")
mcr, lr = j.readIntensity("HeatingLamp_red_.png", "plot-red-heating", "Лампа накаливания", "Красный лист")
mcw, lw = j.readIntensity("HeatingLamp_white_.png", "plot-white-heating", "Лампа накаливания", "Белый лист")
white = lw
mcy, ly = j.readIntensity("HeatingLamp_yellow_.png", "plot-yellow-heating", "Лампа накаливания", "Жёлтый лист")
yellow = ly
# blue = mcb[:, 2] * 0.1144
# red = mcr[:, 0] * 0.2989
# green = mcg[:, 1] * 0.5866
blue = lb
red = lr
green = lg
x = [k * i + b for i in range(len(yellow))]

fig, ax = plt.subplots(figsize=(9, 7), dpi=500)
#Включаем видимость сетки и делений (вводим их параметры ниже(сверху нельзя)
ax.minorticks_on()
#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'both', which = 'major', labelsize = 15, pad = 2, length = 10)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15, pad = 2, length = 5)
#название графика с условием для переноса строки и центрированием
ax.set_title('Отражённая интенсивность излучения лампы накаливания', fontsize = 20, loc = 'center')
#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')
#подпись осей
ax.set_ylabel("Яркость", fontsize = 16)
ax.set_xlabel("Длина волны [нм]", fontsize = 16)
ax.patch.set_facecolor('0.8')
ax.plot(x, blue, 'b', label = "Синий лист")
ax.plot(x, green, 'g', label = "Зелёный лист")
ax.plot(x, red, 'r', label = "Красный лист")
ax.plot(x, white, 'white', label = "Белый лист")
ax.plot(x, yellow, 'y', label = "Жёлтый лист")
ax.legend()
fig.savefig("intensites.png")
fig.clf()

ba = j.albedo(blue, white)
ra = j.albedo(red, white)
ga = j.albedo(green, white)
ya = j.albedo(yellow, white)
for i in range(15):
    ya[len(ya) - i - 1] = 0
wa = [1 for i in range(len(white))]

fig, ax = plt.subplots(figsize=(9, 7), dpi=500)
#Включаем видимость сетки и делений (вводим их параметры ниже(сверху нельзя)
ax.minorticks_on()
#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'both', which = 'major', labelsize = 15, pad = 2, length = 10)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15, pad = 2, length = 5)
#название графика с условием для переноса строки и центрированием
ax.set_title('Альбедо поверхностей', fontsize = 20, loc = 'center')
#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')
#подпись осей
ax.set_ylabel("Яркость", fontsize = 16)
ax.set_xlabel("Длина волны [нм]", fontsize = 16)
ax.patch.set_facecolor('0.85')
ax.plot(x, ba, 'b', label = "Синий лист")
ax.plot(x, ga, 'g', label = "Зелёный лист")
ax.plot(x, ra, 'r', label = "Красный лист")
ax.plot(x, wa, 'white', label = "Белый лист")
ax.plot(x, ya, 'y', label = "Жёлтый лист")
ax.legend()
fig.savefig("albedos.png")
fig.clf()

# Построение графика интенсивностей и альбедо
#j.intensities(mn)
