import { useNavigate } from 'react-router-dom';
import type { EvaluationReport } from '../api/evaluation';

interface ReportCardProps {
  report: EvaluationReport;
  onClose: () => void;
}

export default function ReportCard({ report, onClose }: ReportCardProps) {
  const navigate = useNavigate();

  const passedPercentage = Math.round(report.completion_percentage);
  const allPassed = report.all_passed;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-90 flex items-center justify-center p-4 z-50">
      <div className="bg-surface border-2 border-primary rounded-2xl max-w-3xl w-full max-h-[90vh] overflow-y-auto">
        <div className="p-8">
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold bg-gradient-to-r from-[#6B4FFF] to-[#FF6EC7] bg-clip-text text-transparent mb-2">
              Evaluation Report Card
            </h1>
            <p className="text-gray-400">Your skill assessment results</p>
          </div>

          {/* Overall Score */}
          <div className="bg-background rounded-xl p-6 mb-6 border-2 border-primary border-opacity-30">
            <div className="text-center">
              <div className="text-6xl font-bold mb-2">
                <span className={allPassed ? 'text-success' : 'text-secondary'}>
                  {passedPercentage}%
                </span>
              </div>
              <p className="text-xl text-gray-300">
                {allPassed ? '🎉 Perfect Score!' : `${report.skills_passed} of ${report.total_skills} skills passed`}
              </p>
            </div>
          </div>

          {/* Results Summary */}
          <div className="grid grid-cols-2 gap-4 mb-6">
            <div className="bg-success bg-opacity-10 border border-success rounded-lg p-4">
              <div className="text-2xl font-bold text-success mb-1">
                {report.skills_passed}
              </div>
              <div className="text-sm text-gray-400">Skills Mastered</div>
            </div>
            <div className="bg-red-500 bg-opacity-10 border border-red-500 rounded-lg p-4">
              <div className="text-2xl font-bold text-red-400 mb-1">
                {report.skills_tested - report.skills_passed}
              </div>
              <div className="text-sm text-gray-400">Skills to Study</div>
            </div>
          </div>

          {/* Passed Skills */}
          {report.passed_skills.length > 0 && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-3 text-success">
                ✅ Skills You've Mastered
              </h3>
              <div className="bg-background rounded-lg p-4 space-y-2">
                {report.passed_skills.map((skill) => (
                  <div
                    key={skill.skill_id}
                    className="flex items-center gap-2 text-sm text-gray-300"
                  >
                    <span className="text-success">✓</span>
                    {skill.skill_name}
                  </div>
                ))}
              </div>
              <p className="text-xs text-gray-500 mt-2">
                You can skip these topics on Khan Academy
              </p>
            </div>
          )}

          {/* Failed Skill - Where to Start */}
          {report.failed_skill && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-3 text-red-400">
                📚 Start Studying Here
              </h3>
              <div className="bg-red-500 bg-opacity-10 border-2 border-red-500 rounded-lg p-4">
                <div className="font-semibold text-lg mb-2">
                  {report.failed_skill.skill_name}
                </div>
                <div className="text-sm text-gray-400 space-y-1">
                  <p>Your answer: <span className="text-red-400">{report.failed_skill.user_answer}</span></p>
                  <p>Correct answer: <span className="text-success">{report.failed_skill.correct_answer}</span></p>
                </div>
              </div>
              <p className="text-sm text-gray-400 mt-2">
                💡 Begin your Khan Academy studies with this topic
              </p>
            </div>
          )}

          {/* All Passed Message */}
          {allPassed && (
            <div className="bg-success bg-opacity-10 border-2 border-success rounded-lg p-6 mb-6 text-center">
              <p className="text-lg text-success font-semibold mb-2">
                Outstanding! You've mastered all available skills!
              </p>
              <p className="text-sm text-gray-400">
                You're ready to move on to more advanced topics
              </p>
            </div>
          )}

          {/* Action Buttons */}
          <div className="flex gap-3">
            <button
              onClick={() => {
                onClose();
                navigate('/progress');
              }}
              className="flex-1 btn-secondary"
            >
              View Progress
            </button>
            <button
              onClick={onClose}
              className="flex-1 btn-primary"
            >
              Start Practice Mode
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
