# EN MOSTAFA AI AGENT v2.1 - Professional Architecture Guide

هذه الوثيقة تصف المعمارية العامة للريبو بشكل احترافي. الهدف ليس تقديم النظام كأداة WordPress فقط، بل كمنصة Agent محلية قابلة للتوسع لإدارة المواقع، تشغيل مهام النظام، التعامل مع الملفات، تنفيذ PowerShell/CMD، بناء وتعديل مشاريع برمجية بلغات مختلفة، وربط نماذج لغوية متعددة مثل ChatGPT/OpenAI وClaude/Anthropic والنماذج المحلية أو المزودات المتوافقة مع OpenAI.

## 1. الفكرة الأساسية

EN MOSTAFA AI AGENT هو Local AI Control Agent. يعمل كطبقة وسيطة بين المستخدم والنظام المحلي والخدمات الخارجية.

WordPress هو Adapter من ضمن الـ adapters، وليس حدود النظام بالكامل. نفس البنية يمكن استخدامها لإدارة:

- مواقع WordPress أو LMS أو Hostinger أو أي REST API خارجي.
- ملفات ومجلدات محلية داخل Windows.
- أوامر PowerShell وCMD.
- مشاريع Python وJavaScript وPHP وC# وASP.NET.
- عمليات قراءة/كتابة كود، تشغيل اختبارات، بناء مشاريع، وتحضير تكامل مع Visual Studio.
- موصلات LLM مختلفة عبر طبقة واحدة قابلة للتبديل.

## 2. حالة الريبو الحالية وحدودها

هذا الريبو `v2.1` هو foundation نظيف وخفيف. الملفات الحالية تنفذ هيكل REST/Dashboard/LLM placeholder بشكل صغير ومفهوم:

| الملف | الدور الحالي |
|---|---|
| `src/app.py` | نقطة دخول Flask وتشغيل السيرفر على `127.0.0.1:5001`. |
| `src/routes.py` | تسجيل REST endpoints الخاصة بالمهام وchat وحالة المواقع. |
| `src/wp_manager.py` | أول Adapter خارجي، حاليًا لتسجيل مواقع WordPress وفحص الحالة بشكل مبسط. |
| `src/llm_bridge.py` | حدود الاتصال مع النموذج اللغوي. حاليًا mock/placeholder وجاهز للاستبدال بموصلات حقيقية. |
| `templates/dashboard.html` | Dashboard بسيط لإظهار حالة النسخة وروابط الفحص. |
| `requirements.txt` | اعتماديات Python الأساسية: Flask وrequests وpython-dotenv. |
| `docs/roadmap.md` | خريطة التطوير المقترحة. |

الطبقات المتقدمة مثل MCP Server وTask Engine وMemory وStrategy وPlanning وAutonomous Loop مذكورة هنا كمعمارية توسع مقصودة. هذه الأسماء مستخدمة في النسخة الممتدة من النظام ويمكن نقلها تدريجيًا لهذا الريبو عند الانتقال من prototype إلى production runtime.

## 3. النظرة المعمارية العليا

```text
-------------------+       +----------------------+
| User / Operator  | <---> | Dashboard / REST API |
| Browser / VS     |       | Flask app.py         |
+-------------------+       +----------+-----------+
                                      |
                                      v
                         +------------+-------------+
                         | Agent Gateway             |
                         | routes.py                 |
                         +------------+-------------+
                                      |
              +-----------------------+-----------------------+
              |                       |                       |
              v                       v                       v
   +----------+----------+  +---------+----------+  +---------+----------+
   | LLM Bridge          |  | Integration       |  | Local Automation  |
   | ChatGPT/Claude/etc. |  | Adapters          |  | PowerShell/CMD    |
   +----------+----------+  +---------+----------+  +---------+----------+
              |                       |                       |
              v                       v                       v
   +----------+----------+  +---------+----------+  +---------+----------+
   | Tool-Use / MCP      |  | WordPress, LMS,   |  | Files, builds,    |
   | function calls      |  | Hosting, APIs     |  | tests, code       |
   +---------------------+  +--------------------+  +--------------------+
```

المعمارية تتعامل مع كل Capability كأداة قابلة للاستدعاء. النموذج اللغوي لا يجب أن يخمن، بل يطلب أداة، والأداة تنفذ، ثم ترجع نتيجة قابلة للتحقق.

## 4. شرح الطبقات الأساسية

### 4.1 REST API Layer

في النسخة الحالية، `src/app.py` ينشئ تطبيق Flask، و`src/routes.py` يسجل Blueprint باسم `/wp`.

Endpoints الحالية:

| Endpoint | الدور |
|---|---|
| `GET /` | فتح Dashboard. |
| `GET /healthz` | فحص سريع لحالة السيرفر. |
| `GET /wp/sites` | عرض المواقع المسجلة في `WPManager`. |
| `POST /wp/operator/run` | تنفيذ مهمة نصية عبر `LLMBridge.execute_task`. |
| `GET /wp/status?site=...` | جلب حالة موقع مسجل. |
| `POST /wp/ai/chat` | إرسال رسالة Chat للـ LLM bridge. |

في النسخة الإنتاجية، REST يصبح public control surface للتكامل مع Dashboard أو ASP.NET أو أدوات خارجية. أمثلة endpoints المتوقعة:

- `/run` لتنفيذ مهمة عامة.
- `/system/status` لحالة النظام.
- `/llm/status` و`/llm/configure` لإدارة موصلات النماذج.
- `/knowledge/upload` لإضافة ملفات معرفة.
- `/wp/*` كـ WordPress adapter.
- `/hostinger/*` كـ Hosting adapter.

### 4.2 MCP Layer

MCP هو طبقة أدوات موجهة للنماذج والـ AI clients. وظيفته ليست استبدال REST، بل إعطاء النماذج واجهة tool calling موحدة.

في المعمارية الإنتاجية يكون الملف المقابل عادة:

| الملف | الدور |
|---|---|
| `mcp_server.py` | FastMCP/SSE server يعرض أدوات للملفات، shell، browser، WordPress، screenshots، OCR، والذاكرة. |
| `llm_tools.py` | تعريف أدوات LLM وتنفيذها داخليًا، حتى يستطيع ChatGPT/Claude طلب أداة بدل توليد نص فقط. |
| `tool_manifest.py` | وصف قدرات الأدوات، سياسات retry، وأفضل مسار لكل نوع مهمة. |
| `tool_registry.py` | تسجيل الأدوات ومراقبة حالتها وعدد الاستدعاءات والأخطاء. |

مثال تدفق MCP:

```text
LLM asks: run_powershell({ script: "dotnet build" })
MCP validates policy
Tool executes locally
Tool returns stdout/stderr/exit code
LLM summarizes verified result
```

هذه الطبقة تجعل النظام مناسبًا لمهام محلية مثل إنشاء مشروع ASP.NET، تعديل ملفات C#، تشغيل `dotnet test`، أو قراءة بنية مشروع من Visual Studio، وليس فقط إدارة WordPress.

### 4.3 LLM Bridge

`src/llm_bridge.py` في الريبو الحالي هو boundary صغير:

- `execute_task(task, site_name=None)` لتنفيذ مهمة.
- `chat(message, site_name=None)` للمحادثة.
- `provider = "mock"` كقيمة افتراضية.

في الإنتاج يتم توسيعه إلى موصلات متعددة:

| Provider | طريقة الربط |
|---|---|
| OpenAI / ChatGPT | OpenAI API أو واجهة متوافقة مع OpenAI chat/tool calling. |
| Anthropic Claude | Messages API مع tool-use. |
| OpenRouter / Groq / DeepSeek / Qwen / Together | OpenAI-compatible APIs غالبًا. |
| Gemini | Google Generative Language API. |
| Ollama | Local model API بدون مفتاح خارجي. |
| Mock | للاختبارات والتطوير بدون تكلفة. |

المبدأ المهم: تغيير النموذج لا يغير باقي النظام. REST وTask Engine وAdapters تتعامل مع `LLMBridge` فقط.

### 4.4 Integration Adapters

`src/wp_manager.py` هو أول Adapter. حاليًا يحتفظ بقائمة مواقع داخل الذاكرة ويقدم:

- `list_sites()`
- `get_site_status(site_name)`
- `add_site(name, url, api_key=None)`

في التوسع، كل نظام خارجي يصبح Adapter مستقل:

| Adapter | أمثلة |
|---|---|
| WordPressAdapter | مواقع، إضافات، مستخدمين، REST plugin endpoints. |
| LMSAdapter | MasterStudy، كورسات، دروس، اختبارات، ملفات تعليمية. |
| HostingAdapter | Hostinger، VPS، domains، DNS، metrics. |
| LocalProjectAdapter | قراءة مشاريع، تعديل ملفات، تشغيل builds/tests. |
| DotNetAdapter | `dotnet new`, `dotnet build`, `dotnet test`, ASP.NET scaffolding. |

بهذا الشكل لا يصبح النظام محبوسًا في WordPress. WordPress مجرد implementation من interface أوسع.

## 5. Task Engine

Task Engine هو طبقة تنفيذ مهام طويلة أو متعددة الخطوات. في النسخة الحالية، `/wp/operator/run` يمرر المهمة مباشرة إلى `LLMBridge`. في الإنتاج، Task Engine يضيف:

- إنشاء `task_id`.
- تقسيم المهمة إلى steps.
- حفظ الحالة في SQLite.
- تنفيذ كل step مع retries.
- تمرير context من خطوة إلى أخرى.
- استئناف المهمة بعد توقف السيرفر.
- إرجاع progress للـ Dashboard.

ملفات الإنتاج المتوقعة:

| الملف | الدور |
|---|---|
| `task_engine.py` | إنشاء المهام والخطوات وحفظها وتنفيذها واستئنافها. |
| `system_executor.py` | تشغيل أوامر CMD/PowerShell مع diagnosis وretries. |
| `outcome_verifier.py` | التحقق من أن الناتج تحقق فعليًا: ملف موجود، URL يعمل، build نجح. |
| `shell_reliability.py` | اختيار shell المناسب وإصلاح مشاكل البيئة. |

تدفق مهمة محلية:

```text
User: "Create an ASP.NET API project and run tests"
REST /run
Task Engine creates task
Planner creates steps:
  1. dotnet new webapi
  2. add controllers/services
  3. dotnet build
  4. dotnet test
SystemExecutor runs commands
OutcomeVerifier checks build/test output
Dashboard shows progress
```

## 6. Memory / Strategy / Planning

هذه الطبقات تجعل الـ Agent يتعلم من التشغيل السابق بدل تنفيذ كل مرة من الصفر.

### Memory

Memory تحفظ تاريخ التنفيذ:

- نص المهمة أو الأمر.
- هل نجح أم فشل.
- مدة التنفيذ.
- الخطأ إن وجد.
- توقيت التنفيذ.

الاستخدام:

- اقتراح أفضل طريقة بناءً على نجاحات سابقة.
- عرض محاولات مشابهة قبل التنفيذ.
- تجنب تكرار أوامر فاشلة.

ملف الإنتاج المقابل: `memory_engine.py`.

### Strategy

Strategy تتعامل مع جودة الطرق المختلفة:

- success rate.
- average duration.
- fallback command عند الفشل.

مثال: إذا فشل `pip install` بطريقة معينة، يمكن اقتراح `py -3.11 -m pip install`.

ملف الإنتاج المقابل: `strategy_engine.py`.

### Planning

Planning يحول الطلب الطبيعي إلى خطة قابلة للتنفيذ:

- تحليل النية.
- اختيار الأدوات.
- ترتيب الخطوات.
- تحديد dependencies.
- تحديد المخاطر.

ملفات الإنتاج المقابلة:

| الملف | الدور |
|---|---|
| `planning_graph.py` | بناء graph للخطوات وترتيب dependencies. |
| `decision_engine.py` | اختيار المهمة التالية أو مسار recovery. |
| `dynamic_rules.py` | تعلم قواعد بسيطة من الأخطاء وتطبيقها على أوامر لاحقة. |
| `state_manager.py` | تخزين الحالة الحالية: المهمة، الخطوات، النتيجة. |

## 7. Autonomous Loop

Autonomous Loop هو نمط تشغيل مستمر، وليس مجرد endpoint واحد. وظيفته إدارة backlog من الأهداف والمهام.

تدفقه المنطقي:

```text
while running:
  task = GoalManager.get_next_task()
  if no task:
      SelfImprovementEngine.generate_improvement_tasks()
      sleep
      continue

  result = AgentCore.handle_task(task)
  if result completed:
      GoalManager.mark_task_done(task)

  SelfMonitor.evaluate_task(result)
  SelfMonitor.suggest_improvements()
```

ملفات الإنتاج المقابلة:

| الملف | الدور |
|---|---|
| `autonomous_loop.py` | الحلقة المستمرة التي تسحب المهام وتنفذها. |
| `goal_manager.py` | إدارة قائمة الأهداف والمهام. |
| `agent_core.py` | تنسيق brain/executor/memory/strategy/rules. |
| `self_monitor.py` | تقييم النتائج واقتراح تحسينات. |
| `self_improvement.py` | توليد مهام تحسين ذاتي عند عدم وجود مهام مباشرة. |

يجب تشغيل هذا النمط بحذر في production، خصوصًا مع أوامر النظام أو المواقع الحقيقية. الأفضل أن تكون الأفعال الخطرة gated بوضوح عبر confirm أو approval policy.

## 8. Dashboard

`templates/dashboard.html` حاليًا شاشة بسيطة تعرض:

- اسم النظام.
- حالة Prototype.
- روابط `healthz` و`/wp/sites`.

في النسخة الإنتاجية، Dashboard يصبح Control Center:

- اختيار البيئة أو الموقع أو المشروع المحلي.
- Live status للسيرفر وMCP وLLM provider.
- Task queue مع progress.
- سجل Activity.
- AI chat مرتبط بالأدوات.
- إدارة LLM keys/providers.
- إدارة ملفات ومشاريع محلية.
- تشغيل أوامر آمنة ومشاهدة النتائج.
- WordPress/LMS/Hosting كصفحات adapters منفصلة.

مهم: الواجهة لا يجب أن تكون مقيدة بصفحة WordPress. يجب أن تعرض WordPress كقسم من أقسام النظام، إلى جانب Local Projects وPowerShell وMCP وLLM وHosting.

## 9. Visual Studio وASP.NET Integration

يمكن ربط النظام مع Visual Studio أو مشاريع ASP.NET بثلاث طرق:

1. REST API من داخل تطبيق ASP.NET أو tool داخلي.
2. MCP connector بحيث يستطيع AI client تشغيل أدوات المشروع.
3. PowerShell/CMD tasks لتشغيل `dotnet`, `msbuild`, `nuget`, وملفات solution.

مثال ASP.NET client:

```csharp
using System.Net.Http.Json;

var client = new HttpClient
{
    BaseAddress = new Uri("http://127.0.0.1:5001")
};

var payload = new
{
    task = "Analyze this ASP.NET project, run dotnet build, and report errors",
    site = (string?)null
};

var result = await client.PostAsJsonAsync("/wp/operator/run", payload);
var body = await result.Content.ReadAsStringAsync();
Console.WriteLine(body);
```

في النسخة الحالية سيعود الرد من mock LLM. بعد إضافة Task Engine وSystemExecutor يصبح نفس endpoint قادرًا على تنفيذ خطوات فعلية محليًا.

## 10. التشغيل

تشغيل النسخة الحالية:

```powershell
cd C:\mcp-agent\en-mostafa-ai-agent-v2.1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src\app.py
```

فتح Dashboard:

```text
http://127.0.0.1:5001
```

فحص الصحة:

```powershell
Invoke-RestMethod http://127.0.0.1:5001/healthz
```

تشغيل مهمة:

```powershell
Invoke-RestMethod `
  -Method POST `
  -Uri http://127.0.0.1:5001/wp/operator/run `
  -ContentType "application/json" `
  -Body '{"task":"analyze local project structure","site":null}'
```

## 11. مبادئ الأمان

- Local-first: لا ترسل ملفات أو أسرار خارجية إلا عبر provider مضبوط صراحة.
- Secrets مثل API keys يجب أن تكون في `.env` أو config خاص غير مرفوع للريبو.
- أوامر shell الخطرة يجب أن تتطلب confirmation.
- لا تستخدم النموذج اللغوي لاتخاذ قرار destructive بدون تحقق.
- افصل Adapters عن Task Engine حتى لا تؤثر مهمة WordPress على مشروع محلي أو العكس.
- اجعل كل نتيجة قابلة للتحقق: status code، exit code، file exists، tests pass.

## 12. اتجاه التطوير المقترح

الترتيب العملي لتحويل هذا الريبو من foundation إلى agent production:

1. إضافة config layer لـ LLM providers.
2. استبدال mock في `src/llm_bridge.py` بموصل OpenAI/Claude/OpenAI-compatible.
3. إضافة `TaskEngine` بسيط مع SQLite.
4. إضافة `SystemExecutor` لتشغيل PowerShell/CMD بأمان.
5. إضافة `MCP Server` اختياري لعرض نفس الأدوات للـ AI clients.
6. توسيع Dashboard لعرض tasks/logs/provider status.
7. فصل WordPress كـ adapter مستقل، ثم إضافة adapters أخرى مثل ASP.NET projects وHostinger.
8. إضافة Memory/Strategy/Planning بعد وجود تنفيذ حقيقي يمكن التعلم منه.

## 13. الخلاصة المعمارية

هذا الريبو يجب تقديمه كمنصة Agent عامة قابلة للتوسع:

- REST API للتطبيقات والداشبورد.
- MCP tools للنماذج والـ AI clients.
- LLM Bridge قابل لتبديل المزود.
- Task Engine لتنفيذ مهام طويلة.
- Memory/Strategy/Planning للتعلم والتحسين.
- Local Automation لتشغيل PowerShell/CMD وإدارة مشاريع برمجية.
- Adapters خارجية، منها WordPress وLMS وHosting، وليست هي جوهر النظام الوحيد.

---
