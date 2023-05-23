from AutoGeneratingScetches import AutoGenScetches

Generator = AutoGenScetches(10, 10)
Generator.LoadPhotoAndScetch()
#Generator.makeViewedScetch()
Generator.GenerateP()
Generator.MakeFirstScetchGeneration()
Generator.MakeSecondScetchGeneration()
Generator.CalculateSSIM()
Generator.ShowResults()