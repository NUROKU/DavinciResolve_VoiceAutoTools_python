timeline = resolve.GetProjectManager() \
            .GetCurrentProject() \
            .GetCurrentTimeline()
            
mediapool = resolve.GetProjectManager() \
            .GetCurrentProject() \
            .GetMediaPool()

timeline.SetCurrentTimecode("01:02:00:00")


#clip = mediapool.ImportMedia(r"C:\Users\shimau6\Downloads\あかりちゃん立ち絵_0000.png")
#subClip = {
#    "mediaPoolItem": clip,
#    "startFrame": 0,
#    "endFrame": 23,
#}
#mediapool.AppendToTimeline([ subClip ])

timeline.InsertFusionTitleIntoTimeline("Text+")
#timeline.SetTrackLock
#timeline.InsertTitleIntoTimeline("text")

print(timeline.GetCurrentTimecode())


