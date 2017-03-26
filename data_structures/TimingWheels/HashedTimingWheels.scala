
trait AsyncOperation{

  val timeToExpire : Int

  def expire : Unit = {}

}

class DataBaseOperation(expireTime : Int ) extends AsyncOperation{

  timeToExpire = expireTime

}

class TimeOutManager{

  var currentTick : Int = 1

  var timeWheel: Map[Char,AsyncOperation] = Map()

  def addOperation(asyncOperation: AsyncOperation) : Unit = {

  }

  def expireOperation : Unit = {

    timeWheel

  }

}


