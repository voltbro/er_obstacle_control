# er_obstacle_control
Контроль столкновения для робота TurtleBro

# Установка
```sh
cd catkin_ws/src/
git clone https://github.com/voltbro/er_obstacle_control.git 
cd ..
catkin_make --pkg=er_obstacle_control
```
```sh
cd catkin_ws/src/er_obstacle_control/script/
sudo chmod +x er_run.py
```


# Запуск

```sh
roslaunch er_obstacle_control er.launch
```

# Использование


Команды которые должны быть вызваны через методы вызова rosservice call.
Структура данных следующая:
er_event_request: int64

пример использования:
```sh
rosservice call /er_obstacle_control "er_event_request: 1"
```

Ответ от сервиса:
resp: string

O - препятствие отсутствует/несущественное
l - препятствие присутствует
2 - неверный запрос
