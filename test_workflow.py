from app.workflow.ai_workflow import AIWorkflow

workflow = AIWorkflow()

result = workflow.run_workflow("NAFLD")

print("\nFinal Result")
print(result)
