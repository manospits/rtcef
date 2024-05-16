package ui.experiments.exposed2cli.cards.archived.inc

import model.waitingTime.ForecastMethod
import ui.experiments.exposed2cli.ConfigExp
import ui.experiments.exposed2cli.cards.Constants

object ConfigsSPSAIncGT {
  val configSPSAFixed = new ConfigExp(
    domain               = "cards",
    patternFilePath      = Constants.wayebHome + "/patterns/feedzai/increasing/patternGT.sre",
    patternName          = "increasingGTSPSAFixed",
    declarationsFilePath = Constants.wayebHome + "/patterns/feedzai/increasing/declarationsLT.sre",
    resultsDir           = Constants.dataDir + "/results",
    orders               = List(1, 2, 3, 4),
    horizon              = 200,
    distances            = List(1, 2, 3, 4, 5, 6, 7).map(x => (x.toDouble, x.toDouble)),
    maxSpreads           = List(0, 2, 4, 6),
    thresholds           = List(0.0, 0.25, 0.5, 0.75),
    foldsDir             = Constants.dataDir + "/enriched/increasingGT/folds",
    folds                = List(1, 2, 3, 4),
    spreadMethod         = ForecastMethod.FIXEDSPREAD,
    maxNoStatesList      = List(1000)
  )

  val configSPSAMax = new ConfigExp(
    domain               = "cards",
    patternFilePath      = Constants.wayebHome + "/patterns/feedzai/increasing/patternGT.sre",
    patternName          = "increasingGTSPSAMax",
    declarationsFilePath = Constants.wayebHome + "/patterns/feedzai/increasing/declarationsLT.sre",
    resultsDir           = Constants.dataDir + "/results",
    orders               = List(1, 2, 3, 4),
    horizon              = 200,
    maxSpreads           = List(0, 2, 4, 6),
    thresholds           = List(0.0, 0.25, 0.5, 0.75),
    foldsDir             = Constants.dataDir + "/enriched/increasingGT/folds",
    folds                = List(1, 2, 3, 4),
    spreadMethod         = ForecastMethod.SMARTSCAN,
    maxNoStatesList      = List(1000)
  )

  val configs: List[ConfigExp] = List(configSPSAMax, configSPSAFixed) // configSPSAMax

}
