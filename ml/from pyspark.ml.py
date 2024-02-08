from pyspark.ml.evaluation import MulticlassClassificationEvaluator

def evaluate_metrics(func):
    def wrapper(predictions_df):
        evaluator = MulticlassClassificationEvaluator()
        
        accuracy = evaluator.evaluate(predictions_df, {evaluator.metricName: "accuracy"})
        print("Accuracy:", accuracy)

        labels = [0, 1, 2]
        print("\nIndividual class metrics:")
        for label in sorted(labels):
            print("Class %s" % (label))
            precision = evaluator.evaluate(predictions_df, {evaluator.metricLabel: label,
                                                            evaluator.metricName: "precisionByLabel"})
            print("\tPrecision:", precision)
            recall = evaluator.evaluate(predictions_df, {evaluator.metricLabel: label,
                                                         evaluator.metricName: "recallByLabel"})
            print("\tRecall:", recall)
            f1 = evaluator.evaluate(predictions_df, {evaluator.metricLabel: label,
                                                     evaluator.metricName: "fMeasureByLabel"})
            print("\tF1 Score:", f1)

        overallPrecision = evaluator.evaluate(predictions_df, {evaluator.metricName: "weightedPrecision"})
        print("Overall Precision:", overallPrecision)
        overallRecall = evaluator.evaluate(predictions_df, {evaluator.metricName: "weightedRecall"})
        print("Overall Recall:", overallRecall)
        overallF1 = evaluator.evaluate(predictions_df, {evaluator.metricName: "weightedFMeasure"})
        print("Overall F1 Score:", overallF1)

        func(predictions_df)
    return wrapper

# Example usage
@evaluate_metrics
def evaluate(predictions_df):
    # Your existing code for inference or any other processing
    pass

# Inference predicted labels from validation data
predictions_df = model.transform(validation_df)

# Call the decorated function
evaluate(predictions_df)
