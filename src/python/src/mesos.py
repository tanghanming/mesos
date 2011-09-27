import sys
import _mesos


# Base class for Mesos schedulers. Users' schedulers should extend this class
# to get default implementations of methods they don't override.
class Scheduler:
  def registered(self, driver, frameworkId): pass
  def resourceOffers(self, driver, offers): pass
  def offerRescinded(self, driver, offerId): pass
  def statusUpdate(self, driver, status): pass
  def frameworkMessage(self, driver, message): pass
  def slaveLost(self, driver, slaveId): pass

  # Default implementation of error() prints to stderr because we can't
  # make error() an abstract method in Python
  def error(self, driver, code, message):
    print >> sys.stderr, "Error from Mesos: %s (code: %d)" % (message, code)


# Interface for Mesos scheduler drivers. Users may wish to extend this class
# in mock objects for tests.
class SchedulerDriver:
  def start(self): pass
  def stop(self, failover = False): pass
  def abort(self) : pass
  def join(self): pass
  def run(self): pass
  def requestResources(self, requests): pass
  def launchTasks(self, offerId, tasks, filters = None): pass
  def killTask(self, taskId): pass
  def reviveOffers(self): pass
  def sendFrameworkMessage(self, slaveId, executorId, data): pass


# Base class for Mesos executors. Users' executors should extend this class
# to get default implementations of methods they don't override.
class Executor:
  def init(self, driver, args): pass
  def launchTask(self, driver, task): pass
  def killTask(self, driver, taskId): pass
  def frameworkMessage(self, driver, message): pass
  def shutdown(self, driver): pass

  # Default implementation of error() prints to stderr because we can't
  # make error() an abstract method in Python
  def error(self, driver, code, message):
    print >> sys.stderr, "Error from Mesos: %s (code: %d)" % (message, code)


# Interface for Mesos executor drivers. Users may wish to extend this class
# in mock objects for tests.
class ExecutorDriver:
  def start(self): pass
  def stop(self, failover = False): pass
  def abort(self): pass
  def join(self): pass
  def run(self): pass
  def sendStatusUpdate(self, status): pass
  def sendFrameworkMessage(self, data): pass


# Alias the MesosSchedulerDriverImpl from _mesos. Ideally we would make this
# class inherit from SchedulerDriver somehow, but this complicates the C++
# code, and there seems to be no point in doing it in a dynamic language.
MesosSchedulerDriver = _mesos.MesosSchedulerDriverImpl


# Alias the MesosExecutorDriverImpl from _mesos. Ideally we would make this
# class inherit from ExecutorDriver somehow, but this complicates the C++
# code, and there seems to be no point in doing it in a dynamic language.
MesosExecutorDriver = _mesos.MesosExecutorDriverImpl
