import VideoPlayer from './VideoPlayer';

interface LearnModalProps {
  skillId: number;
  skillName: string;
  subject: string;
  youtubeId?: string;
  explanation?: string;
  khanUrl?: string;
  onClose: () => void;
}

export default function LearnModal({
  skillName,
  subject,
  youtubeId,
  explanation,
  khanUrl,
  onClose,
}: LearnModalProps) {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-95 flex items-center justify-center p-2 sm:p-4 z-50 safe-area-inset">
      <div className="bg-surface border border-gray-700 rounded-xl max-w-4xl w-full max-h-[95vh] overflow-y-auto touch-scroll">
        {/* Header */}
        <div className="sticky top-0 bg-surface border-b border-gray-700 px-4 sm:px-6 py-4 flex items-center justify-between">
          <div>
            <h2 className="text-xl sm:text-2xl font-bold text-white">{skillName}</h2>
            <p className="text-sm text-gray-400">{subject}</p>
          </div>
          <button
            onClick={onClose}
            className="p-2 text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-white/5"
            aria-label="Close"
          >
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Content */}
        <div className="p-4 sm:p-6 space-y-6">
          {/* Video Section */}
          {youtubeId ? (
            <div>
              <h3 className="text-lg font-semibold text-white mb-3 flex items-center gap-2">
                <span className="text-2xl">🎥</span> Video Lesson
              </h3>
              <VideoPlayer youtubeId={youtubeId} title={skillName} />
            </div>
          ) : (
            <div className="bg-gray-800 rounded-lg p-6 text-center">
              <div className="text-4xl mb-3">📚</div>
              <p className="text-gray-400 mb-4">
                Video lesson coming soon! For now, you can learn on Khan Academy.
              </p>
              {khanUrl && (
                <a
                  href={khanUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-primary inline-block"
                >
                  Learn on Khan Academy →
                </a>
              )}
            </div>
          )}

          {/* Explanation Section */}
          {explanation && (
            <div>
              <h3 className="text-lg font-semibold text-white mb-3 flex items-center gap-2">
                <span className="text-2xl">💡</span> Quick Explanation
              </h3>
              <div className="bg-background rounded-lg p-4 border border-gray-700">
                <p className="text-gray-300 leading-relaxed">{explanation}</p>
              </div>
            </div>
          )}

          {/* Khan Academy Link */}
          {khanUrl && (
            <div className="bg-primary bg-opacity-10 rounded-lg p-4 border border-primary border-opacity-30">
              <h4 className="font-semibold text-primary mb-2">Want to learn more?</h4>
              <p className="text-sm text-gray-400 mb-3">
                Khan Academy has full courses, practice exercises, and more videos on this topic.
              </p>
              <a
                href={khanUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 text-primary hover:text-primary-light transition-colors"
              >
                <span>Continue on Khan Academy</span>
                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </a>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="sticky bottom-0 bg-surface border-t border-gray-700 px-4 sm:px-6 py-4">
          <button
            onClick={onClose}
            className="w-full btn-secondary"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
