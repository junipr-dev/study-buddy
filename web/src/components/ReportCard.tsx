import { useNavigate } from 'react-router-dom';
import type { EvaluationReport, SkillResult } from '../api/evaluation';

interface ReportCardProps {
  report: EvaluationReport;
  onClose: () => void;
}

function SkillItem({ skill, showScore = true }: { skill: SkillResult; showScore?: boolean }) {
  const levelColors: Record<string, string> = {
    mastered: 'text-success',
    proficient: 'text-blue-400',
    developing: 'text-orange-400',
    study: 'text-red-400',
  };

  return (
    <div className="flex items-center justify-between py-2 border-b border-gray-800 last:border-0">
      <div>
        <span className="text-gray-300">{skill.skill_name}</span>
        <span className="text-xs text-gray-500 ml-2">({skill.subject})</span>
      </div>
      {showScore && (
        <div className="flex items-center gap-2">
          <span className="text-xs text-gray-500">
            {skill.questions_correct}/{skill.questions_total}
          </span>
          <span className={`font-semibold ${levelColors[skill.proficiency_level] || 'text-gray-400'}`}>
            {skill.proficiency_score}%
          </span>
        </div>
      )}
    </div>
  );
}

export default function ReportCard({ report, onClose }: ReportCardProps) {
  const navigate = useNavigate();

  const studyCount = report.study?.length || 0;
  const developingCount = report.developing?.length || 0;
  const proficientCount = report.proficient?.length || 0;
  const masteredCount = report.mastered?.length || 0;

  const allMastered = studyCount === 0 && developingCount === 0;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-90 flex items-center justify-center p-2 sm:p-4 z-50 safe-area-inset">
      <div className="bg-surface border-2 border-primary rounded-2xl max-w-3xl w-full max-h-[95vh] sm:max-h-[90vh] overflow-y-auto touch-scroll">
        <div className="p-4 sm:p-8">
          {/* Header */}
          <div className="text-center mb-4 sm:mb-8">
            <h1 className="text-2xl sm:text-4xl font-bold bg-gradient-to-r from-[#6B4FFF] to-[#FF6EC7] bg-clip-text text-transparent mb-2">
              Evaluation Report Card
            </h1>
            <p className="text-sm sm:text-base text-gray-400">Comprehensive skill assessment results</p>
          </div>

          {/* Overall Score */}
          <div className="bg-background rounded-xl p-6 mb-6 border-2 border-primary border-opacity-30">
            <div className="text-center">
              <div className="text-6xl font-bold mb-2">
                <span className={report.overall_score >= 80 ? 'text-success' : report.overall_score >= 50 ? 'text-yellow-400' : 'text-red-400'}>
                  {report.overall_score}%
                </span>
              </div>
              <p className="text-xl text-gray-300 mb-1">
                {allMastered ? 'Outstanding!' : `${report.total_correct} of ${report.total_questions} questions correct`}
              </p>
              <p className="text-sm text-gray-500">
                {report.total_skills_tested} skills tested
              </p>
            </div>
          </div>

          {/* Results Summary Grid - 4 columns for 4 proficiency levels */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 mb-4 sm:mb-6">
            <div className="bg-success bg-opacity-10 border border-success rounded-lg p-3 text-center">
              <div className="text-2xl font-bold text-success mb-1">
                {masteredCount}
              </div>
              <div className="text-xs text-gray-400">Mastered</div>
              <div className="text-xs text-gray-500">Level 3</div>
            </div>
            <div className="bg-blue-500 bg-opacity-10 border border-blue-500 rounded-lg p-3 text-center">
              <div className="text-2xl font-bold text-blue-400 mb-1">
                {proficientCount}
              </div>
              <div className="text-xs text-gray-400">Proficient</div>
              <div className="text-xs text-gray-500">Level 2</div>
            </div>
            <div className="bg-orange-500 bg-opacity-10 border border-orange-500 rounded-lg p-3 text-center">
              <div className="text-2xl font-bold text-orange-400 mb-1">
                {developingCount}
              </div>
              <div className="text-xs text-gray-400">Developing</div>
              <div className="text-xs text-gray-500">Level 1</div>
            </div>
            <div className="bg-red-500 bg-opacity-10 border border-red-500 rounded-lg p-3 text-center">
              <div className="text-2xl font-bold text-red-400 mb-1">
                {studyCount}
              </div>
              <div className="text-xs text-gray-400">Need Study</div>
              <div className="text-xs text-gray-500">Failed</div>
            </div>
          </div>

          {/* Study Recommendation */}
          <div className="bg-primary bg-opacity-10 border border-primary rounded-lg p-4 mb-6">
            <h3 className="font-semibold mb-2 text-primary">Study Recommendation</h3>
            <p className="text-gray-300">{report.study_recommendation}</p>
          </div>

          {/* Skills Needing Study - Failed Level 1 */}
          {studyCount > 0 && report.study && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-3 text-red-400">
                Priority Study Areas ({studyCount})
              </h3>
              <div className="bg-background rounded-lg p-4">
                {report.study.map((skill) => (
                  <SkillItem key={skill.skill_id} skill={skill} />
                ))}
              </div>
              <p className="text-xs text-gray-500 mt-2">
                Focus on these first - they need the most attention
              </p>
            </div>
          )}

          {/* Developing Skills - Passed Level 1 only */}
          {developingCount > 0 && report.developing && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-3 text-orange-400">
                Developing Skills ({developingCount})
              </h3>
              <div className="bg-background rounded-lg p-4">
                {report.developing.map((skill) => (
                  <SkillItem key={skill.skill_id} skill={skill} />
                ))}
              </div>
              <p className="text-xs text-gray-500 mt-2">
                Good start - practice these to reach proficiency
              </p>
            </div>
          )}

          {/* Proficient Skills - Passed Level 2 */}
          {proficientCount > 0 && report.proficient && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-3 text-blue-400">
                Proficient Skills ({proficientCount})
              </h3>
              <div className="bg-background rounded-lg p-4 max-h-40 overflow-y-auto">
                {report.proficient.map((skill) => (
                  <SkillItem key={skill.skill_id} skill={skill} />
                ))}
              </div>
              <p className="text-xs text-gray-500 mt-2">
                Solid understanding - a bit more practice for mastery
              </p>
            </div>
          )}

          {/* Mastered Skills - Passed Level 3 */}
          {masteredCount > 0 && report.mastered && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-3 text-success">
                Mastered Skills ({masteredCount})
              </h3>
              <div className="bg-background rounded-lg p-4 max-h-40 overflow-y-auto">
                {report.mastered.map((skill) => (
                  <SkillItem key={skill.skill_id} skill={skill} />
                ))}
              </div>
              <p className="text-xs text-gray-500 mt-2">
                Excellent! You can skip these topics on Khan Academy
              </p>
            </div>
          )}

          {/* All Mastered Message */}
          {allMastered && (
            <div className="bg-success bg-opacity-10 border-2 border-success rounded-lg p-6 mb-6 text-center">
              <p className="text-lg text-success font-semibold mb-2">
                Outstanding! You've demonstrated proficiency across all tested skills!
              </p>
              <p className="text-sm text-gray-400">
                You're ready to move on to more advanced topics or challenge yourself with harder problems.
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
