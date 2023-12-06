# def stop():
#     print("stop")
# def start():
#     print(start)
# def pause():
#     print("pasuse")
#
# command = "Stop"
#
# # ## buď takhle ale to je špatně protože moc podmínke, raději to vnořím to slovníku
# # if command == "stop"
# #     stop()
# # elif command == "start"
# #     start()
# # elif command == "pause"
#
# ## nebo takhle
#
# to_execute = {"Stop" : stop,
#            "Start" : start,
#            "Pause" : pause}
# to_execute[command]()

##########################################

# jak udělat dataklass, buď použiju tohle a nebo ten dataklas
import dataclasses

#
# class Person:
#     def __init__(self, name, surename):
#         self.name = name
#         self.surename = surename
# new_person = Person("alex", "doe")
# # druhá verze

#
# @dataclasses.dataclass # tohle je dekorátor, to z toho dělá ten dataclass
# class Person:
#     name: str
#     surname: str = "Doe"
#     def __post_init__(self): # jejich vyhodu že mají tuto metodu kdy potom co se zinicializujou tak mužu ještě něco udělat.
#         print("init_done")
#
# new_person = Person("Alex")



# jak udělat dokumentaci
    