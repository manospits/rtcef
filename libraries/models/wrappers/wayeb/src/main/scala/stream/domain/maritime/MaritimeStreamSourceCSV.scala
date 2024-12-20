package stream.domain.maritime

import com.typesafe.scalalogging.LazyLogging
import stream.source.{EmitMode, StreamSource, CSVStreamSource}
import stream.{GenericEvent, ResetEvent}

object MaritimeStreamSourceCSV {
  /**
    * Constructor for maritime stream source.
    *
    * @param filename The path to the file.
    * @return The stream source.
    */
  def apply(filename: String): MaritimeStreamSourceCSV = new MaritimeStreamSourceCSV(filename)
}

/**
  * Stream source for maritime trajectories given in a single csv file.
  *
  * @param filename The path to the file.
  */
class MaritimeStreamSourceCSV(filename: String) extends CSVStreamSource(filename) with LazyLogging {

  override def line2Event(
                           line: Seq[String],
                           id: Int
                         ): GenericEvent = {
    try {
      val timestamp = line(0).toLong
      val mmsi = line(1).toString
      val lon = line(2).toDouble
      val lat = line(3).toDouble
      val speed = line(4).toDouble
      val heading = line(5).toDouble
      val cog = line(6).toDouble
      val annotation = line(7)
      val nextCETimestamp = if (line.size > 8) line(8).toLong else -1
      if (timestamp == -1) ResetEvent(Map("mmsi" -> mmsi))
      else {
        val ge = GenericEvent(id, "SampledCritical", timestamp,
                              Map("mmsi" -> mmsi, "speed" -> speed, "lon" -> lon, "lat" -> lat, "heading" -> heading,
            "cog" -> cog, "annotation" -> annotation, "nextCETimestamp" -> nextCETimestamp))
        ge
      }
    } catch {
      case e: Exception => {
        logger.warn("COULD NOT PARSE LINE " + line)
        throw new Error
      }
    }
  }

}
