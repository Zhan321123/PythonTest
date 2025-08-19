import psutil


def getEquipmentInfo():
  cpuPercent = psutil.cpu_percent(interval=1)  # 获取CPU使用率（百分比） interval=1 表示监测1秒内的平均使用率
  memory = psutil.virtual_memory()  # 获取内存使用率信息
  memory_percent = memory.percent  # 内存使用率（百分比）
  used_memory = round(memory.used / (1024 ** 3), 2)  # 已使用内存（GB）
  total_memory = round(memory.total / (1024 ** 3), 2)  # 总内存（GB）
  physical_cores = psutil.cpu_count(logical=False) #
  logical_cores = psutil.cpu_count(logical=True) #
  processes = list(psutil.process_iter())
  process_count = len(processes)
  thread_count = sum(p.num_threads() for p in processes)
  handle_count = sum(p.num_handles() for p in processes)
  cpu_cores = psutil.cpu_percent(percpu=True, interval=0.1)

  battery = psutil.sensors_battery()

  return {

    'CPU使用率': cpuPercent,
    '内存使用率': memory_percent,
    '已使用内存（GB）': used_memory,
    '总内存（GB）': total_memory,

    "电量": f"{battery.percent}%",
    "充电状态": "充电中" if battery.power_plugged else "未充电",
    "剩余时间": f"{round(battery.secsleft / 3600, 1)} 小时" if not battery.power_plugged else "未知"

  }
