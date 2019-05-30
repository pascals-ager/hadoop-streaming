val metaSettings = Seq(
  name := "hadoop-streaming",
    version := "0.1"
)

val scalaSettings = Seq(
  scalaVersion := "2.12.8",
  scalacOptions ++= Seq("-feature", "-unchecked", "-deprecation", "-encoding", "utf8")
)

val dependencies = Seq("org.scalactic" %% "scalactic" % "3.0.5",
  "org.scalatest" %% "scalatest" % "3.0.5" % "test")

lazy val root = (project in file("."))
  .settings(metaSettings: _*)
  .settings(scalaSettings: _*)
  .settings(libraryDependencies ++= dependencies)